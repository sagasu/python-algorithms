from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        # Sort nodes by value. Edge i-j exists iff |nums[i]-nums[j]| <= maxDiff,
        # so on the sorted line each node can jump to any other within maxDiff.
        # Shortest path from left to right = min jumps with greedy furthest reach.
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for s, i in enumerate(order):
            pos[i] = s

        # reach[s] = rightmost sorted index reachable in one jump from s
        reach = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and nums[order[j + 1]] - nums[order[i]] <= maxDiff:
                j += 1
            reach[i] = j

        # Binary lifting: up[k][i] = position after 2^k furthest jumps from i
        log = max(1, n.bit_length())
        up = [reach[:]]
        for k in range(1, log):
            prev = up[k - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def min_jumps(left: int, right: int) -> int:
            if left == right:
                return 0
            # Furthest position reachable with any number of jumps
            if up[-1][left] < right:
                return -1

            cur = left
            ans = 0
            for k in range(log - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    ans += 1 << k
            return ans + 1

        result = []
        for u, v in queries:
            if u == v:
                result.append(0)
                continue
            left, right = pos[u], pos[v]
            if left > right:
                left, right = right, left
            result.append(min_jumps(left, right))
        return result
