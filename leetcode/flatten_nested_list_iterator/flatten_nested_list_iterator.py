class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nl):
            integers = []
            for i in nl:
                if i.isInteger():
                    integers.append(i.getInteger())
                else:
                    integers.extend(flatten(i.getList()))
            return integers
        self.n = deque(flatten(nestedList))
    
    def next(self) -> int:
        return self.n.popleft()
    
    def hasNext(self) -> bool:
        return self.n