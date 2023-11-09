class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 1
        ret = 0
        
        for i in range(1,len(s)):
            if  s[i] == s[i-1]:
                count+=1
            else:
                ret+= ((count+1) * count) // 2
                count = 1
        ret += ((count+1) * count) // 2

        return ret % (10 ** 9 + 7)