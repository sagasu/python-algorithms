# Project rules

## Python

Do **not** use `python`, `python3`, or `py` from PATH. On this machine those resolve to Windows Store stubs and fail.

Use Anaconda Python directly:

```text
D:\worek\anaconda3\python.exe
```

Example:

```powershell
& "D:\worek\anaconda3\python.exe" path\to\script.py
```

Other envs exist under `D:\worek\anaconda3\envs\` if a specific env is needed; default base is fine for leetcode solutions.
