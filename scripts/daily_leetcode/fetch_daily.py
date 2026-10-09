"""Fetch today's LeetCode daily challenge.

Exit codes:
  0  a new problem was written to --out
  2  this slug already has a Python solution locally or on origin/feature/dailyProblem
  1  the challenge could not be fetched
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

REPO = Path(r"D:\worek\repos\python-algorithms")
BRANCH = "feature/dailyProblem"
ENDPOINT = "https://leetcode.com/graphql"
QUERY = """
query questionOfToday {
  activeDailyCodingChallengeQuestion {
    date
    link
    question {
      questionId
      questionFrontendId
      title
      titleSlug
      difficulty
      content
      exampleTestcases
      topicTags { name slug }
      codeSnippets { lang langSlug code }
    }
  }
}
"""


def normalize(name: str) -> str:
    return name.replace("-", "_").replace(" ", "_").lower()


def python_files_in(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return [path for path in directory.glob("*.py") if path.is_file()]


def local_solution(title_slug: str) -> str | None:
    root = REPO / "leetcode"
    target = normalize(title_slug)
    if not root.is_dir():
        return None
    for child in root.iterdir():
        if child.is_dir() and normalize(child.name) == target and python_files_in(child):
            return str(child)
    return None


def origin_solution(title_slug: str) -> str | None:
    target = normalize(title_slug)
    try:
        completed = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", f"origin/{BRANCH}", "leetcode"],
            cwd=REPO,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    for line in completed.stdout.splitlines():
        parts = line.split("/")
        if len(parts) < 3 or parts[0] != "leetcode" or not line.endswith(".py"):
            continue
        if normalize(parts[1]) == target:
            return line
    return None


def fetch_challenge() -> dict:
    # This Anaconda build cannot load _ssl, so HTTPS goes through curl.exe.
    curl = shutil.which("curl.exe") or shutil.which("curl")
    if not curl:
        raise RuntimeError("curl.exe is not on PATH")
    completed = subprocess.run(
        [
            curl,
            "-sS",
            "--max-time",
            "45",
            "-X",
            "POST",
            ENDPOINT,
            "-H",
            "Content-Type: application/json",
            "-H",
            "User-Agent: Mozilla/5.0 (compatible; daily-leetcode/1.0)",
            "-H",
            "Referer: https://leetcode.com/problemset/",
            "--data",
            json.dumps({"query": QUERY}),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout or "").strip()
        raise RuntimeError(f"LeetCode request failed: {detail}")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"LeetCode returned non-JSON: {completed.stdout[:200]}") from exc
    if payload.get("errors"):
        raise RuntimeError(json.dumps(payload["errors"]))
    challenge = (payload.get("data") or {}).get("activeDailyCodingChallengeQuestion")
    if not challenge or not challenge.get("question"):
        raise RuntimeError("LeetCode returned no active daily challenge")
    return challenge


def python_stub(question: dict) -> str:
    for snippet in question.get("codeSnippets") or []:
        if snippet.get("langSlug") == "python3":
            return snippet.get("code") or ""
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    try:
        challenge = fetch_challenge()
    except Exception as exc:
        print(f"fetch error: {exc}")
        return 1

    question = challenge["question"]
    slug = question.get("titleSlug") or ""
    if not slug:
        print("fetch error: daily challenge has no titleSlug")
        return 1

    existing = local_solution(slug) or origin_solution(slug)
    link = challenge.get("link") or f"/problems/{slug}/"
    if link.startswith("/"):
        link = "https://leetcode.com" + link

    record = {
        "date": challenge.get("date"),
        "link": link,
        "questionFrontendId": question.get("questionFrontendId"),
        "title": question.get("title"),
        "titleSlug": slug,
        "folder": normalize(slug),
        "difficulty": question.get("difficulty"),
        "content": question.get("content") or "",
        "exampleTestcases": question.get("exampleTestcases") or "",
        "topicTags": question.get("topicTags") or [],
        "python3Stub": python_stub(question),
        "alreadySolved": existing,
    }
    Path(args.out).write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    if existing:
        print(f"already solved: {existing}")
        return 2
    print(f"new: {record['title']} ({slug})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
