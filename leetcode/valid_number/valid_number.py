class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()

        def isDecimal(s):
            if isInteger(s):
                return True
            if len(s) == 0:
                return False
            if s[0] in "+-":
                s = s[1:]
            if len(s) == 0:
                return False
            if s.count(".") != 1:
                return False

            first, second = s.split(".")
            if len(first) == 0 and len(second) == 0:
                return False
            if len(first) > 0 and len(second) > 0:
                return isInteger(first) and isInteger(second, True)
            if len(first) > 0:
                return isInteger(first)
            return isInteger(second, True)

        def isInteger(s, signed=False):
            if len(s) == 0:
                return False
            if s[0] in "+-":
                if signed:
                    return False
                s = s[1:]
            if len(s) == 0:
                return False
            return all(x.isdigit() for x in s)
        if s.count("e") == 0:
            return isDecimal(s)
        if s.count("e") > 1:
            return False
        first, second = s.split("e")
        return isDecimal(first) and isInteger(second)
                
        
