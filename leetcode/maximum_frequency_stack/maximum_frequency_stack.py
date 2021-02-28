from sortedcontainers import SortedList

class FreqStack:

    def __init__(self):
        self.stack_by_number = collections.defaultdict(list)
        self.time = 0
        self.sorted_list = SortedList()

    def push(self, x: int) -> None:
        self.time += 1
        if len(self.stack_by_number[x]) > 0:
            self.sorted_list.remove((len(self.stack_by_number[x]), self.stack_by_number[x][-1], x))
        self.stack_by_number[x].append(self.time)
        self.sorted_list.add((len(self.stack_by_number[x]), self.stack_by_number[x][-1], x))

    def pop(self) -> int:
        last_item = self.sorted_list[-1]
        x = last_item[2]

        self.sorted_list.remove(last_item)
        self.stack_by_number[x].pop()
        if len(self.stack_by_number[x]) > 0:
            self.sorted_list.add((len(self.stack_by_number[x]), self.stack_by_number[x][-1], x))
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()