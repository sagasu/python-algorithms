class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        sv = []
        idxs = []
        for i, c in enumerate(s):
            if c in vowels:
                sv.append((ord(c), c))
                idxs.append(i)

        s = list(s)                
        for i, v in zip(idxs, sorted(sv)):
            s[i] = v[1]
       
        return "".join(s)