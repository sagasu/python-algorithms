class ReachNumber:
    def reachNumber(self, target):
        count = 0

        for i in range(888888):
            count += i

            if abs(target) <= abs(count) and target % 2 == count % 2:
                return i