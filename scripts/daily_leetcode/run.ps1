# Daily LeetCode agent.
# Fetches the current daily challenge, solves it in a detached worktree,
# and pushes one commit to origin/feature/dailyProblem on GitHub.
# Requires the user to be logged on. Git must already be able to push to origin.

$ErrorActionPreference = "Stop"

$Repo = "D:\worek\repos\python-algorithms"
$Python = "D:\worek\anaconda3\python.exe"
$Grok = "C:\Users\mattk\.grok\bin\grok.exe"
$Branch = "feature/dailyProblem"
$LogDir = Join-Path $env:LOCALAPPDATA "daily-leetcode"
$Worktree = Join-Path $LogDir "worktree"
$Lock = Join-Path $LogDir "run.lock"
$Log = Join-Path $LogDir "runs.log"

function Write-Log([string]$Message) {
    $line = "{0} {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Message
    Add-Content -Path $Log -Value $line -Encoding utf8
    Write-Host $line
}

function Remove-Worktree {
    if (Test-Path $Worktree) {
        & git -C $Repo worktree remove --force $Worktree
        if ($LASTEXITCODE -ne 0) {
            Write-Log "worktree remove failed; deleting the directory"
            Remove-Item -Recurse -Force $Worktree -ErrorAction SilentlyContinue
            & git -C $Repo worktree prune
        }
    }
}

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

if (Test-Path $Lock) {
    $ageHours = ((Get-Date) - (Get-Item $Lock).LastWriteTime).TotalHours
    if ($ageHours -lt 6) {
        Write-Log "skip: a run is already in progress"
        exit 0
    }
    Write-Log "removing a stale lock"
}
Set-Content -Path $Lock -Value $PID -Encoding ascii

$exitCode = 0
try {
    if (-not (Test-Path $Python)) {
        Write-Log "missing python: $Python"
        exit 1
    }
    if (-not (Test-Path $Grok)) {
        Write-Log "missing grok: $Grok"
        exit 1
    }

    $env:GIT_TERMINAL_PROMPT = "0"
    $env:GCM_INTERACTIVE = "Never"

    # Drop a worktree left by a previous failed run. Logs stay in $LogDir.
    Remove-Worktree

    Write-Log "fetching origin/$Branch"
    & git -C $Repo fetch origin $Branch
    if ($LASTEXITCODE -ne 0) {
        Write-Log "git fetch failed"
        exit 1
    }

    $problemPath = Join-Path $LogDir "today.json"
    & $Python (Join-Path $Repo "scripts\daily_leetcode\fetch_daily.py") --out $problemPath
    $fetchCode = $LASTEXITCODE
    if ($fetchCode -eq 2) {
        Write-Log "already solved; nothing to push"
        exit 0
    }
    if ($fetchCode -ne 0) {
        Write-Log "fetch failed with exit $fetchCode"
        exit $fetchCode
    }

    $problem = Get-Content -Path $problemPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $folder = [string]$problem.folder
    $title = [string]$problem.title
    if ([string]::IsNullOrWhiteSpace($folder) -or [string]::IsNullOrWhiteSpace($title)) {
        Write-Log "problem JSON is missing folder or title"
        exit 1
    }

    Remove-Worktree
    Write-Log "creating worktree at $Worktree"
    & git -C $Repo worktree add --detach $Worktree "origin/$Branch"
    if ($LASTEXITCODE -ne 0) {
        Write-Log "worktree add failed"
        exit 1
    }

    $promptTemplate = Get-Content -Path (Join-Path $Repo "scripts\daily_leetcode\prompt.txt") -Raw -Encoding UTF8
    $promptPath = Join-Path $LogDir "prompt-today.txt"
    [System.IO.File]::WriteAllText($promptPath, $promptTemplate.Replace("{{PROBLEM_JSON}}", $problemPath))

    $grokLog = Join-Path $LogDir ("grok-{0:yyyyMMdd-HHmmss}.log" -f (Get-Date))
    Write-Log "solving $title"
    & $Grok --prompt-file $promptPath --cwd $Worktree --yolo --no-auto-update --max-turns 40 --output-format json --deny "Bash(git*)" --deny "Bash(Remove-Item *)" --deny "Bash(rm *)" *> $grokLog
    $grokCode = $LASTEXITCODE
    Write-Log "grok exit $grokCode (log $grokLog)"

    $solution = Join-Path $Worktree "leetcode\$folder\$folder.py"
    if (-not (Test-Path $solution)) {
        Write-Log "no solution file at leetcode/$folder/$folder.py"
        exit 1
    }

    Write-Log "running example tests"
    & $Python $solution
    if ($LASTEXITCODE -ne 0) {
        Write-Log "example tests failed; not pushing"
        exit 1
    }

    $relative = "leetcode/$folder/$folder.py"
    $status = @(& git -C $Worktree status --porcelain | Where-Object { $_ })
    $headFiles = @(& git -C $Worktree diff --name-only "origin/$Branch" -- | Where-Object { $_ })
    $alreadyCommitted = ($status.Count -eq 0 -and $headFiles.Count -eq 1 -and $headFiles[0] -eq $relative)
    if ($alreadyCommitted) {
        Write-Log "solution is already the only new commit"
    } else {
        $extraStatus = @($status | Where-Object { $_ -notmatch [regex]::Escape($relative) })
        if ($extraStatus.Count -gt 0 -or $headFiles.Count -gt 0) {
            Write-Log ("refusing to commit because other files changed: " + (($status + $headFiles) -join ", "))
            exit 1
        }

        & git -C $Worktree add -- $relative
        if ($LASTEXITCODE -ne 0) {
            Write-Log "git add failed"
            exit 1
        }

        $staged = @(& git -C $Worktree diff --cached --name-only | Where-Object { $_ })
        if ($staged.Count -ne 1 -or $staged[0] -ne $relative) {
            Write-Log ("refusing to commit unexpected files: " + ($staged -join ", "))
            exit 1
        }

        & git -C $Worktree commit -m $title
        if ($LASTEXITCODE -ne 0) {
            Write-Log "git commit failed"
            exit 1
        }
    }

    Write-Log "pushing to origin $Branch"
    & git -C $Worktree push origin "HEAD:$Branch"
    if ($LASTEXITCODE -ne 0) {
        Write-Log "git push failed"
        exit 1
    }

    Write-Log "pushed $title ($relative)"
    Remove-Worktree
}
catch {
    Write-Log ("error: " + $_.Exception.Message)
    $exitCode = 1
}
finally {
    Remove-Item -Force $Lock -ErrorAction SilentlyContinue
}

exit $exitCode
