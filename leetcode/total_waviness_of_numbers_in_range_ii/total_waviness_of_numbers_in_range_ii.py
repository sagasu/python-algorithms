from functools import cache


class Solution:
    def totalWaviness(self, l: int, r: int) -> int:
        def f(n: int) -> int:
            """Total waviness of all numbers from 1 to n."""
            s = str(n)
            k = len(s)

            @cache
            def dp(pos: int, prev: int, prev2: int, tight: bool, started: bool) -> tuple:
                """
                Returns (count_of_numbers, total_waviness_sum) for numbers
                formed by digits at positions [pos..k-1].
                
                prev  = last digit placed (-1 if not started)
                prev2 = digit before prev (-1 if fewer than 2 placed)
                tight = whether current prefix equals s[:pos]
                started = whether any non-zero digit has been placed
                """
                if pos == k:
                    return (1, 0)  # one valid number, 0 additional waviness from here

                limit = int(s[pos]) if tight else 9
                total_count = 0
                total_wave = 0

                for d in range(0, limit + 1):
                    new_tight = tight and (d == limit)
                    
                    if not started and d == 0:
                        # Still leading zeros - don't place a real digit
                        c, w = dp(pos + 1, -1, -1, new_tight, False)
                        total_count += c
                        total_wave += w
                    else:
                        # We're placing digit d
                        new_prev2 = prev
                        new_prev = d
                        new_started = True

                        # Check if placing d makes prev a peak or valley
                        # prev is at position pos-1, prev2 at pos-2
                        extra = 0
                        if prev != -1 and prev2 != -1:
                            # prev has both neighbors: prev2 and d
                            if prev > prev2 and prev > d:
                                extra = 1  # peak
                            elif prev < prev2 and prev < d:
                                extra = 1  # valley

                        c, w = dp(pos + 1, new_prev, new_prev2, new_tight, new_started)
                        total_count += c
                        total_wave += w + extra * c

                return (total_count, total_wave)

            _, total = dp(0, -1, -1, True, False)
            dp.cache_clear()
            return total

        return f(r) - f(l - 1)
