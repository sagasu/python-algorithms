class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positives_and_zero = collections.deque()
        negatives = collections.deque()

        for x in nums:
            if x < 0:
                negatives.appendleft(x * x)
            else:
                positives_and_zero.append(x * x)

        ans = []

        while(len(negatives) > 0 and len(positives_and_zero) > 0):
            if positives_and_zero < negatives:
                ans.append(positives_and_zero.popleft())
            else:
                ans.append(negatives.popleft())

        # one of them is empty so order doesn't matter
        ans += positives_and_zero + negatives
        return ans