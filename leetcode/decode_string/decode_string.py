class Solution:
    def decodeString(self, s):
        def decode(i):
            ans = ""
            while i < len(s) and s[i] != ']':
                while i < len(s) and s[i].isalpha():
                    ans += s[i]
                    i += 1
                if i >= len(s) or s[i] == ']': continue
                n = ""
                while i < len(s) and s[i].isdigit():
                    n += s[i]
                    i += 1
                tmp, i = decode(i+1)
                ans += tmp * int(n)
            return (ans, i+1)
        return decode(0)[0]