class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = set(int(d) for d in digits)
        dLen = len(digits)
        nStr = str(n)
        nLen = len(nStr)
        
        res = sum(dLen**i for i in range(1, nLen)) # lower dimensions
        
        def helper(firstDigit, slots):
            if slots == 1:
                return sum(d <= firstDigit for d in digits)

            return sum(d < firstDigit for d in digits) * dLen**(slots - 1)
        
        for i in range(nLen):
            curDigit = int(nStr[i])

            res += helper(curDigit, nLen - i)
            
            if not curDigit in digits: # makes no sense to continue
                break
    
        return res