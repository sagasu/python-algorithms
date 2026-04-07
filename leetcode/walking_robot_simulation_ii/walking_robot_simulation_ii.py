class Robot:
    def __init__(self, width: int, height: int):
        # Precompute all perimeter positions with their facing direction.
        # Order: bottom edge E, right edge N, top edge W, left edge S
        # Note: (0,0) at index 0 gets direction 'South' (after a full loop),
        # but initially the robot faces 'East' — handled via isOrigin flag.
        self.pos = (
            [((x, 0), 'East') for x in range(width)]          # bottom: left to right
            + [((width-1, y), 'North') for y in range(1, height)]  # right: bottom to top
            + [((x, height-1), 'West') for x in range(width-2, -1, -1)]  # top: right to left
            + [((0, y), 'South') for y in range(height-2, 0, -1)]   # left: top to bottom
        )
        self.i = 0
        self.is_origin = True  # special case: initial position faces East

    def step(self, num: int) -> None:
        self.is_origin = False
        self.i = (self.i + num) % len(self.pos)

    def getPos(self) -> list:
        return list(self.pos[self.i][0])

    def getDir(self) -> str:
        if self.is_origin:
            return 'East'
        return self.pos[self.i][1]
