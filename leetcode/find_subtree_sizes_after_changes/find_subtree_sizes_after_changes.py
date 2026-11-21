from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        """DFS tracking last ancestor of each letter to reparent, then subtree sizes."""
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26
        saved = [0] * n
        stack = [(0, False)]
        while stack:
            u, leaving = stack.pop()
            c = ord(s[u]) - 97
            if not leaving:
                saved[u] = last[c]
                if last[c] != -1:
                    new_parent[u] = last[c]
                last[c] = u
                stack.append((u, True))
                for v in children[u]:
                    stack.append((v, False))
            else:
                last[c] = saved[u]

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            stack.extend(new_children[u])
        for u in reversed(order):
            for v in new_children[u]:
                ans[u] += ans[v]
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]),
        ([-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]),
    ]
    failed = False
    for parent, s, expected in tests:
        got = sol.findSubtreeSizes(parent, s)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
