class Solution:
    def intToRoman(self, num: int) -> str:
        mapping_str = """I             1
        IV  4
        V             5
        IX  9
        X             10
        XL  40
        L             50
        XC  90
        C             100
        CD  400
        D             500
        CM  900
        M             1000"""

        mappings = []
        for mapping in mapping_str.split("\n"):
            c,v = mapping.split()
            v = int(v)
            mappings.append((c, v))

        mappings.reverse()
        ans = ""
        for c, v in mappings:
            current, num = divmod(num, v)
            if current > 0:
                ans += c * current 

        return ans