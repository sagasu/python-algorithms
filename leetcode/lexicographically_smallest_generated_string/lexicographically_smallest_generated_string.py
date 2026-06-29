class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        sz = n + m - 1
        ans = [None] * sz
        modifiable = [True] * sz

        # Step 1: force-write str2 at every 'T' position
        for i, tf in enumerate(str1):
            if tf == 'T':
                for j, c in enumerate(str2):
                    pos = i + j
                    if ans[pos] is not None and ans[pos] != c:
                        return ''  # conflict between two 'T' windows
                    ans[pos] = c
                    modifiable[pos] = False

        # Step 2: fill unset positions with 'a'
        for i in range(sz):
            if ans[i] is None:
                ans[i] = 'a'

        # Step 3: for each 'F' position, ensure str2 does NOT match there
        for i in range(n):
            if str1[i] == 'F' and ans[i:i + m] == list(str2):
                # Find the last modifiable position in this window to flip to 'b'
                last_mod = -1
                for j in range(m):
                    if modifiable[i + j]:
                        last_mod = i + j
                if last_mod == -1:
                    return ''  # window is fully locked but matches str2
                ans[last_mod] = 'b'
                modifiable[last_mod] = False

        return ''.join(ans)
