from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.sl = SortedList()

    def book(self, start: int, end: int) -> bool:
        end -= 1
        start_index = self.sl.bisect_left(tuple([start]))
        end_index = self.sl.bisect_left(tuple([end]))

        if start_index != end_index:
            return False

        if 0 <= start_index < len(self.sl):
            x, isEnd = self.sl[start_index]
            isStart = not isEnd

            if not isStart:
                return False

            if start <= x <= end:
                return False

        self.sl.add((start, False))
        self.sl.add((end, True))
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)