from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if not costs:
            return 0
        # Counting sort: find max cost
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1
        # Greedily buy from cheapest
        bought = 0
        for price in range(1, max_cost + 1):
            if count[price] > 0:
                for _ in range(count[price]):
                    if coins >= price:
                        coins -= price
                        bought += 1
                    else:
                        return bought
        return bought