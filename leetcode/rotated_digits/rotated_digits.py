class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = set('347')
        changes = set('2569')

        def is_good(x: int) -> bool:
            digits = str(x)
            return (not any(d in invalid for d in digits) and
                    any(d in changes for d in digits))

        return sum(is_good(x) for x in range(1, n + 1))
