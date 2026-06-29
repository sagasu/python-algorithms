class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ans = []
        N = len(target)
        M = len(stamp)

        stamp = list(stamp)
        old_target = target
        target = list(target)

        def match(offset):
            count = 0
            for i in range(M):
                if stamp[i] != target[i + offset] and target[i + offset] != "*":
                    return False
                if target[i + offset] != "*":
                    count +=1
            return count > 0

        while True:
            found = False

            for start in range(N - M + 1):
                if match(start):
                    found = True
                    for i in range(start, start + M):
                        target[i] = "*"
                    ans.append(start)
                    break

            if all(x == "*" for x in target):
                break

            if not found:
                return []

        ans.reverse()
        constructed = [""] * N
        for index in ans:
            for k in range(M):
                constructed[index + k] = stamp[k]

        if "".join(constructed) == old_target:
            return ans
        return []
        