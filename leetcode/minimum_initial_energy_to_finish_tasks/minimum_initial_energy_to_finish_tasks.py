from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sort by (minimum - actual) ascending = tasks with smallest buffer go last
        # Equivalently sort by (actual - minimum) descending
        tasks.sort(key=lambda t: t[0] - t[1])

        ans = 0
        for actual, minimum in reversed(tasks):
            # We need at least `minimum` energy before this task
            # After finishing it we have (energy - actual) left
            # Working backwards: if we need `ans` energy after this task,
            # we need max(minimum, ans + actual) before it
            ans = max(minimum, ans + actual)

        return ans
