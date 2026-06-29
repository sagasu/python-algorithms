class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        N = len(s)
        def has_leading_zero(s):
            return len(s) > 1 and s[0] == "0"

        def has_trailing_zero(s):
            return s[-1] == "0"

        def get_numbers(s):
            ans = []
            if not has_leading_zero(s):
                ans.append(s)

            for period_index in range(1, len(s)):
                whole, decimal = s[:period_index], s[period_index:]

                if not has_leading_zero(whole) and not has_trailing_zero(decimal):
                    ans.append(f"{whole}.{decimal}")
            return ans
        ans = []
        for coma_index in range(1, N):
            x, y = s[:coma_index], s[coma_index:]
            possible_xs = get_numbers(x)
            possible_ys = get_numbers(y)

            for px in possible_xs:
                for py in possible_ys:
                    ans.append(f"({px}, {py})")

        return ans

