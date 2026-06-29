class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n>0) and ((n&(n-1))==0) and ((n%3==1))
    

print(Solution().isPowerOfFour(5) == False)
print(Solution().isPowerOfFour(99) == False)
print(Solution().isPowerOfFour(16384) == True)
print(Solution().isPowerOfFour(16) == True)
print(Solution().isPowerOfFour(1) == True)
print(Solution().isPowerOfFour(-2147483648) == False)
print(Solution().isPowerOfFour(0) == False)
print(Solution().isPowerOfFour(8) == False)