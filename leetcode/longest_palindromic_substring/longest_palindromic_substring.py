class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest = ""

        for middle in range(N):
            left = middle
            right = middle 

            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1

            if len(s[left +1:right]) > len(longest):
                longest = s[left + 1:right]

            left = middle
            right = middle + 1

            if right >= N or s[left] != s[right]:
                continue

            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1

            if len(s[left +1:right]) > len(longest):
                longest = s[left + 1:right]
        return longest
    
    
print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("a"))