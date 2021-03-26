class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_intersection = collections.Counter()

        for word in B:
            f = collections.Counter(word)

            for c in f.keys():
                b_intersection[c] = max(b_intersection[c], f[c])

        ans = []

        for word in A:
            f = collections.Counter(word)

            if(f & b_intersection) == b_intersection:
                ans.append(word)

        return ans