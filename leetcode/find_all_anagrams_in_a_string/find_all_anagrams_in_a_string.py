class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []
        
        sl = []
        ans = []
        
        pl =[0]*26
        for i in p:
            pl[ord(i)-97]+=1
        
        for ix, i in enumerate(s):
            if not sl:            
                sl = [0]*26         
                for i in s[:len(p)]:
                    sl[ord(i)-97] +=1
                
            else:
                if ix+len(p)-1 < len(s):
                    sl[ord(s[ix-1])-97]-=1
                    sl[ord(s[ix+len(p)-1])-97]+=1
                else:
                    return ans
            if sl == pl:
                ans.append(ix)
        return ans