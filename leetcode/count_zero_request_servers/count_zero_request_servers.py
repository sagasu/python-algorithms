from typing import List


class Solution:
    # Sort queries and slide [q - x, q] over time-sorted logs.
    # Each answer is n minus the distinct servers inside that window.
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda row: row[1])
        order = sorted(range(len(queries)), key=queries.__getitem__)
        ans = [0] * len(queries)
        freq = [0] * (n + 1)
        active = 0
        left = 0
        right = 0
        m = len(logs)
        for idx in order:
            start = queries[idx] - x
            end = queries[idx]
            while right < m and logs[right][1] <= end:
                sid = logs[right][0]
                if freq[sid] == 0:
                    active += 1
                freq[sid] += 1
                right += 1
            while left < right and logs[left][1] < start:
                sid = logs[left][0]
                freq[sid] -= 1
                if freq[sid] == 0:
                    active -= 1
                left += 1
            ans[idx] = n - active
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2]),
        (3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1]),
    ]
    failed = False
    for n, logs, x, queries, expected in tests:
        got = sol.countServers(n, logs, x, queries)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
