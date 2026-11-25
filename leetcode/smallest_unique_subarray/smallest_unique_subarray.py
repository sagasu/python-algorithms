from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        """
        Build a suffix automaton. Identical subarrays share a state, and a
        state that occurs once holds unique subarrays. The shortest of those
        has length link_length + 1; the answer is the minimum such length.
        """
        n = len(nums)
        trans = [{}]
        link = [-1]
        length = [0]
        last = 0
        terminal = []

        for value in nums:
            cur = len(trans)
            trans.append({})
            length.append(length[last] + 1)
            link.append(0)
            p = last
            while p != -1 and value not in trans[p]:
                trans[p][value] = cur
                p = link[p]
            if p == -1:
                link[cur] = 0
            else:
                q = trans[p][value]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(trans)
                    trans.append(dict(trans[q]))
                    length.append(length[p] + 1)
                    link.append(link[q])
                    while p != -1 and trans[p].get(value) == q:
                        trans[p][value] = clone
                        p = link[p]
                    link[q] = clone
                    link[cur] = clone
            last = cur
            terminal.append(cur)

        count = [0] * len(trans)
        for state in terminal:
            count[state] += 1

        by_length = [[] for _ in range(n + 1)]
        for state, state_len in enumerate(length):
            by_length[state_len].append(state)
        for state_len in range(n, 0, -1):
            for state in by_length[state_len]:
                parent = link[state]
                if parent != -1:
                    count[parent] += count[state]

        answer = n
        for state in range(1, len(trans)):
            if count[state] == 1:
                shortest = length[link[state]] + 1
                if shortest < answer:
                    answer = shortest
        return answer


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([3, 3, 3], 3),
        ([2, 1, 2, 3, 3], 1),
        ([1, 1, 2, 2, 1], 2),
    ]
    failed = False
    for nums, expected in tests:
        got = sol.smallestUniqueSubarray(nums)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
