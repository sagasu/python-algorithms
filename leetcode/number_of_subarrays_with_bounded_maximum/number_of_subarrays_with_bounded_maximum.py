class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def countSubarray2(arr):
            N = len(arr)
            return N * (N + 1) // 2

        def countSubarray(arr):
            N = len(arr)
            total = N * (N + 1)//2

            for k,g in groupby(arr, key=lambda x: x >= left):
                if not k:
                    total -= countSubarray2(list(g))

            return total

        N = len(nums)
        total = 0
        for k, g in groupby(nums, key=lambda x:x > right):
            if not k:
                total += countSubarray(list(g))
        return total

    