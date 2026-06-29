class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque()
        sdeadends = set(int(x) for x in deadends)
        if 0 in sdeadends:
            return -1

        dist = {}
        queue.append(0)
        dist[0] = 0

        while len(queue) > 0:
            current = queue.popleft()
            current_positions = [(current //(10 ** index)) % 10 for index in range(4)]

            for index in range(4):
                for delta in [-1, 1]:
                    next_positions = current_positions[:]
                    next_positions[index] += delta
                    next_positions[index] %= 10
                    nxt = reduce(lambda a, x: a * 10 + x, next_positions[::-1])

                    if nxt not in sdeadends and nxt not in dist:
                        queue.append(nxt)
                        dist[nxt] = dist[current] + 1

        if int(target) not in dist:
            return -1
        return dist[int(target)]