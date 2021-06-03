class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        Mod = 10 ** 9 + 7
        hs = horizontalCuts[:]
        hs.append(0)
        hs.append(h)
        hs.sort()

        vs = verticalCuts[:]
        vs.append(0)
        vs.append(w)
        vs.sort()

        maxHeight = max(y2-y1 for y1, y2 in zip(hs, hs[1:]))
        maxWeight = max(x2-x1 for x1, x2 in zip(vs, vs[1:]))

        return (maxHeight * maxWeight) % Mod