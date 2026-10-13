from __future__ import annotations


class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        A +1 or -1 on either array shrinks one absolute gap by 1, so the
        k1 + k2 moves all go to the gaps. x^2 falls by 2x - 1, so the
        largest gap is always the best place to spend the next move.

        Gaps are at most 1e5, so a count of each size walks that peak
        down. That stays linear in the max gap instead of in k (up to 2e9).
        If the budget covers every gap, the sum is 0.
        """
        k = k1 + k2
        freq = [0] * 100001
        total = 0
        max_gap = 0
        for a, b in zip(nums1, nums2):
            gap = abs(a - b)
            freq[gap] += 1
            total += gap
            if gap > max_gap:
                max_gap = gap
        if total <= k:
            return 0

        i = max_gap
        while k > 0 and i > 0:
            if freq[i] == 0:
                i -= 1
                continue
            if k >= freq[i]:
                k -= freq[i]
                freq[i - 1] += freq[i]
                freq[i] = 0
                i -= 1
            else:
                freq[i] -= k
                freq[i - 1] += k
                k = 0

        return sum(count * gap * gap for gap, count in enumerate(freq))


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 2, 3, 4], [2, 10, 20, 19], 0, 0, 579),
        ([1, 4, 10, 12], [5, 8, 6, 9], 1, 1, 43),
    ]
    failed = False
    for nums1, nums2, k1, k2, expected in tests:
        got = sol.minSumSquareDiff(nums1, nums2, k1, k2)
        status = "OK" if got == expected else "FAIL"
        if got != expected:
            failed = True
        print(
            f"{status}: nums1={nums1}, nums2={nums2}, k1={k1}, k2={k2} "
            f"-> {got} (expected {expected})"
        )
    if failed:
        raise SystemExit(1)
