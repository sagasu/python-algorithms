class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        N = len(candyType)
        eaten = set()

        for candy in candyType:
            eaten.add(candy)
            if len(eaten) * 2 >= N:
                return len(eaten)

        return len(eaten)