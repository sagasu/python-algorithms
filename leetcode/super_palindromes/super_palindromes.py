class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        
        count = 0
        current = 1
        while True:
            c = str(current)
            p = int(c + c[:-1][::-1])
            if left  <= (x := p * p) <= right and ((s := str(x)) ==s[::-1]):
                count += 1
            if x > right:
                break

            c = str(current)
            p = int((c + c[::-1]))
            if left <= (x := p * p) <= right and ((s := str(x)) == s[::-1]):
                count +=1
            current += 1
        return count