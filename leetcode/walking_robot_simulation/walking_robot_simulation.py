from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))

        # Directions: N, E, S, W (turn right = +1, turn left = -1 mod 4)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing North
        x = y = 0
        ans = 0

        for cmd in commands:
            if cmd == -2:
                d = (d - 1) % 4
            elif cmd == -1:
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                ans = max(ans, x * x + y * y)

        return ans
