class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        selection = set(arr)
        MOD = 10 ** 9 + 7
        cache = {}

        def numRootedTree(rootVal):
            if rootVal in cache:
                return cache[rootVal]

            count = 1

            for left in selection:
                if rootVal % left == 0:
                    right = rootVal // left
                    if right in selection:
                        count += numRootedTree(left) * numRootedTree(right)
                        count %= MOD
           
            cache[rootVal] = count
            return count

        count = 0

        for root in selection:
            count += numRootedTree(root)
            count %= MOD

        return count