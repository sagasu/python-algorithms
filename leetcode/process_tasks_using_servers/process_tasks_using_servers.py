from __future__ import annotations

import heapq


class Solution:
    # Free heap (weight, index); busy heap (free_time, weight, index).
    # Task j starts at time max(j, next free server).
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = [0] * len(tasks)
        for t, duration in enumerate(tasks):
            while busy and busy[0][0] <= t:
                _, weight, i = heapq.heappop(busy)
                heapq.heappush(free, (weight, i))
            if free:
                weight, i = heapq.heappop(free)
                heapq.heappush(busy, (t + duration, weight, i))
            else:
                free_time, weight, i = heapq.heappop(busy)
                heapq.heappush(busy, (free_time + duration, weight, i))
            ans[t] = i
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 3, 2], [1, 2, 3, 2, 1, 2], [2, 2, 0, 2, 1, 2]),
        ([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1], [1, 4, 1, 4, 1, 3, 2]),
    ]
    failed = False
    for servers, tasks, expected in tests:
        got = sol.assignTasks(servers, tasks)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
