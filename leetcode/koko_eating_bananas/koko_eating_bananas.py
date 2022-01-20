class Solution:
    def minEatingSpeed(self, A: List[int], h: int) -> int:
        def can_eat_all(k):
            return sum(x//k+(1 if x%k!=0 else 0) for x in A)<=h
       
        l,r=1,max(A)
        while l<r:
            mid=(l+r)//2
            if can_eat_all(mid):
                print(mid)
                r=mid
            else:
                l=mid+1
        return l