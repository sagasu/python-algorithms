class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char.islower():  # lowercase English letter
                result.append(char)
            elif char == '*':
                if result:
                    result.pop()
            elif char == '#':
                # Duplicate: append a copy of current result
                result.extend(result[:])
            elif char == '%':
                # Reverse current result
                result.reverse()
        return ''.join(result)