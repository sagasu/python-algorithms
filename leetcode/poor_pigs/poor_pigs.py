class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs,rounds=0,minutesToTest//minutesToDie
        while (rounds+1)**pigs<buckets:
            pigs+=1
        return pigs