from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        """
        Buying a type once grants one free copy of every other item whose
        factor it divides. Extra paid copies add no further freebies, so they
        are only useful on a cheapest type in the purchase.

        Group equal prices and add groups from expensive to cheap. Inside one
        price, keep a prefix of the largest bonuses. A set whose cheapest
        price is p and whose first copies cost c is worth those copies and
        freebies, plus (budget - c) // p extra copies.
        """
        max_factor = 0
        for factor, _price in items:
            if factor > max_factor:
                max_factor = factor

        freq = [0] * (max_factor + 1)
        for factor, _price in items:
            freq[factor] += 1

        # Items whose factor is a multiple of f, including every copy of f.
        cover = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0:
                continue
            total = 0
            for multiple in range(f, max_factor + 1, f):
                total += freq[multiple]
            cover[f] = total

        # cover[f] is the first paid copy plus every free copy that buying f unlocks.
        by_price = [[] for _ in range(1501)]
        for factor, price in items:
            by_price[price].append(cover[factor])

        # dp[c] is the best (paid first copies + freebies) at exact cost c
        # using only prices already considered, all of them >= the next group.
        prev = [-1] * (budget + 1)
        prev[0] = 0
        ans = 0

        for price in range(1500, 0, -1):
            values = by_price[price]
            if not values:
                continue
            values.sort(reverse=True)
            prefix = [0]
            running = 0
            for value in values:
                running += value
                prefix.append(running)

            new = prev[:]
            limit = min(len(values), budget // price)
            for count in range(1, limit + 1):
                cost = count * price
                gained = prefix[count]
                for spent in range(budget - cost + 1):
                    base = prev[spent]
                    if base < 0:
                        continue
                    total_cost = spent + cost
                    score = base + gained
                    if score > new[total_cost]:
                        new[total_cost] = score
                    total = score + (budget - total_cost) // price
                    if total > ans:
                        ans = total
            prev = new

        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[6, 2], [2, 6], [3, 4]], 9, 4),
        ([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8, 10),
    ]
    failed = False
    for items, budget, expected in tests:
        got = sol.maximumSaleItems(items, budget)
        if got == expected:
            print("OK")
        else:
            print("FAIL")
            failed = True
    if failed:
        raise SystemExit(1)
