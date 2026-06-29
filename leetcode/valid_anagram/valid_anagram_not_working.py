class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getFreqMap(s):
            sHash = {}
            for c in s:
                if c in sHash:
                    sHash[c] += 1
                else:
                    sHash[c] = 1
            return sHash

        sHash = getFreqMap(s)
        tHash = getFreqMap(t)

        for key in sHash.keys():
            if sHash[key] != tHash[key]:
                return False

        if len(sHash) != len(tHash):
            return False

        return True