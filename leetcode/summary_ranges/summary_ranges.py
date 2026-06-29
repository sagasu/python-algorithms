from typing import List

class Solution():
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (len(nums) == 0):
            return []

        # this is a hacky way to handle the last element in for statement below. Because last element is not being added, we add one last at the end.
        nums.append(float('inf'))
        ranges = []
        start = nums[0]
        previous = nums[0]
        counter = 0

        for num in nums[1:]:
            if(num != previous + 1):
                if(previous == start):
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{previous}")
                start = num
            previous = num
            counter += 1

        return ranges
