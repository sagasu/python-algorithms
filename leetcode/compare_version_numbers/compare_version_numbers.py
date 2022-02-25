class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        max_len = max(len(v1), len(v2))
        for i in range(max_len):
            c1 = v1[i] if i < len(v1) else 0
            c2 = v2[i] if i < len(v2) else 0

            if c1 != c2:
                return -1 if c1 < c2 else 1
            
        return 0