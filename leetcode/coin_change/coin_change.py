class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        coins.sort()
        inf = 10 * 10

        cache = [[inf] * (amount + 1) for _ in range(N + 1)]
        has_cache = [[False] * (amount + 1) for _ in range(N + 1)]

        # O(N * amount)  time
        # O(N * amount)  space
        def minChange(index, target):
            if target == 0:
                return 0

            if target < 0:
                return inf

            if index == N:
                return inf

            if has_cache[index][target]:
                return cache[index][target]

            current_coin = coins[index]
            least = inf

            least = min(least, minChange(index, target - current_coin) + 1)

            least = min(least, minChange(index + 1, target))


            has_cache[index][target] = True
            cache[index][target] = least
            return least
        least = minChange(0, amount)
        if least >= inf:
            return -1
        return least