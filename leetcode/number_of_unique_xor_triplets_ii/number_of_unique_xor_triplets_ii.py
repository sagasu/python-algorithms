from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        """
        Count distinct values of nums[i] ^ nums[j] ^ nums[k] over i <= j <= k.

        Key insight: index reuse (i==j or j==k) only produces values already in
        the array. Every triple of values (a, b, c) from the distinct set U is
        achievable, so the answer is |{a ^ b ^ c : a, b, c in U}|.

        nums[i] <= 1500 => XOR results fit in [0, 2047]. Build all pairwise XORs,
        then XOR each with every value in U.
        """
        # Presence of values; range is small
        present = [False] * 2048
        for x in nums:
            present[x] = True
        vals = [x for x in range(2048) if present[x]]

        # All pairwise XORs a ^ b for a, b in U (includes a ^ a == 0)
        pair = [False] * 2048
        for i, a in enumerate(vals):
            for b in vals[i:]:
                pair[a ^ b] = True
        pair_vals = [x for x in range(2048) if pair[x]]

        # All triple XORs (a ^ b) ^ c
        trip = [False] * 2048
        for p in pair_vals:
            for c in vals:
                trip[p ^ c] = True

        return sum(trip)
