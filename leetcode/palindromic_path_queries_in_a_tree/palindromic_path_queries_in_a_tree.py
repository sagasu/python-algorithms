from __future__ import annotations


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        """
        A path rearranges into a palindrome iff at most one character has an odd count.
        Root-to-node parity masks live in an Euler-tour Fenwick tree so a character
        update XORs one subtree. Path u-v is prefix[u] XOR prefix[v] XOR char[lca].
        """
        adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        log = 17
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack: list[tuple[int, int, bool]] = [(0, -1, True)]
        while stack:
            u, p, enter = stack.pop()
            if enter:
                parent[u] = u if p < 0 else p
                depth[u] = 0 if p < 0 else depth[p] + 1
                tin[u] = timer
                timer += 1
                stack.append((u, p, False))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, True))
            else:
                tout[u] = timer - 1

        up = [parent[:]]
        for _ in range(1, log):
            prev = up[-1]
            up.append([prev[prev[u]] for u in range(n)])

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1
            if u == v:
                return u
            for k in range(log - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return parent[u]

        bit = [0] * (n + 2)

        def add(i: int, val: int) -> None:
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def pref(i: int) -> int:
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_xor(left: int, right: int, val: int) -> None:
            add(left + 1, val)
            add(right + 2, val)

        chars = [ord(ch) - 97 for ch in s]
        for u in range(n):
            range_xor(tin[u], tout[u], 1 << chars[u])

        ans: list[bool] = []
        for query in queries:
            op, a, b = query.split()
            u = int(a)
            if op == "update":
                c = ord(b) - 97
                old = chars[u]
                if old != c:
                    range_xor(tin[u], tout[u], (1 << old) ^ (1 << c))
                    chars[u] = c
            else:
                v = int(b)
                w = lca(u, v)
                mask = pref(tin[u] + 1) ^ pref(tin[v] + 1) ^ (1 << chars[w])
                ans.append((mask & (mask - 1)) == 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (
            3,
            [[0, 1], [1, 2]],
            "aac",
            ["query 0 2", "update 1 b", "query 0 2"],
            [True, False],
        ),
        (
            4,
            [[0, 1], [0, 2], [0, 3]],
            "abca",
            ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"],
            [False, False, True],
        ),
    ]
    failed = False
    for n, edges, s, queries, expected in tests:
        got = sol.palindromePath(n, edges, s, queries)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
