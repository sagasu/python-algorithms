from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        # Sieve of Eratosthenes
        is_prime = [False, False] + [True] * (max_val - 1)
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False

        # Group indices by value
        val_to_indices = defaultdict(list)
        for i, v in enumerate(nums):
            val_to_indices[v].append(i)

        dist = [-1] * n
        dist[0] = 0
        q = deque([0])
        prime_used = set()  # primes whose teleportation has been fully expanded

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            # Adjacent steps
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and dist[ni] == -1:
                    dist[ni] = d + 1
                    q.append(ni)

            # Prime teleportation: if nums[i] is prime, jump to all multiples
            v = nums[i]
            if is_prime[v] and v not in prime_used:
                prime_used.add(v)
                # All indices whose value is a multiple of v
                for mult in range(v, max_val + 1, v):
                    for idx in val_to_indices[mult]:
                        if dist[idx] == -1:
                            dist[idx] = d + 1
                            q.append(idx)

        return -1
