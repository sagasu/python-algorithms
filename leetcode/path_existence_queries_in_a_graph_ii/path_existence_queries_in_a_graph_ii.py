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

        # Binary lifting: up[k][i] = position after 2^k furthest jumps from i.
        # Need 2^(log-1) >= n so long chains (up to n-1 hops) are covered;
        # n.bit_length() alone is one short for n > 2^(L-1) (e.g. n=1e5).
        log = max(1, n.bit_length() + 1)
        up = [reach[:]]
        for k in range(1, log):
            prev = up[k - 1]
            up.append([prev[prev[i]] for i in range(n)])

        def min_jumps(left: int, right: int) -> int:
            if left == right:
                return 0
            # Take largest jumps that still land strictly before right, then +1.
            # Final hop must actually reach; otherwise a gap blocks the path.
            cur = left
            ans = 0
            for k in range(log - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    ans += 1 << k
            if reach[cur] >= right:
                return ans + 1
            return -1

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
