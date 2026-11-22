from __future__ import annotations

import heapq


class Solution:
    # Busy min-heap of (free_time, id); idle min-heap of virtual ids so the
    # next free server is the first in wrap-around order from i % k.
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        idle = list(range(k))
        busy = []
        count = [0] * k
        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                heapq.heappush(idle, i + (server - i) % k)
            if not idle:
                continue
            server = heapq.heappop(idle) % k
            heapq.heappush(busy, (start + load[i], server))
            count[server] += 1
        busiest = max(count)
        return [i for i, c in enumerate(count) if c == busiest]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3], [1]),
        (3, [1, 2, 3, 4], [1, 2, 1, 2], [0]),
        (3, [1, 2, 3], [10, 12, 11], [0, 1, 2]),
    ]
    failed = False
    for k, arrival, load, expected in tests:
        got = sol.busiestServers(k, arrival, load)
        if sorted(got) == sorted(expected):
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
