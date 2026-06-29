class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left == []:
            left = [0]
        if right == []:
            right = [n]
        if left == [0] and right == [0]:
            return 0
        return max(max(left), n-min(right))