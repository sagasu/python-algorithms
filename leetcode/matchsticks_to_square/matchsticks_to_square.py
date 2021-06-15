class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        N = len(matchsticks)

        perimeter = sum(matchsticks)
        if (perimeter % 4) != 0:
            return False

        sperimeter = perimeter // 4
        if any(x > sperimeter for x in matchsticks):
            return False

        def recurse(index, sides):
            if any(x> sperimeter for x in sides):
                return False
            if index == N:
                return True
            for sideIndex in range(4):
                sides[sideIndex] += matchsticks[index]
                if recurse(index + 1, sides):
                    return True
                sides[sideIndex] -= matchsticks[index]
            return False
        return recurse(0,[0,0,0,0])