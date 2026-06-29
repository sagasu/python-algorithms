class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        return any(Counter(s2[tail - len(s1):tail]) == s1_count for tail in range(len(s1), len(s2) + 1))