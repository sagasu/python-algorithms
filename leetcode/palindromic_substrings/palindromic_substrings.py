class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        count = 0

        for mid in range(N):
            left = mid
            right = mid
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
                count +=1

            if mid + 1 < N:
                left = mid
                right = mid +1

                while left >= 0 and right < N and s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1

        return count