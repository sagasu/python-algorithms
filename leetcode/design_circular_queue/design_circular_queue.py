class MyCircularQueue:

    def __init__(self, k: int):
        self.deque = collections.deque()
        self.k = k        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0
        

    def isFull(self) -> bool:
        return len(self.deque) == self.k