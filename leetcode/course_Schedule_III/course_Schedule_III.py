class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        best = 0
        timeSpent = 0
        h = []

        current = 0
        courses.sort(key=lambda x: x[1])

        for duration, last in courses:
            heapq.heappush(h, -duration)
            timeSpent += duration
            current += 1
            while timeSpent > last and len(h) > 0:
                timeSpent -= -heapq.heappop(h)
                current -= 1

            best = max(best, current)
        return best