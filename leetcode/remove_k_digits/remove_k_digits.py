class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'
        else:
            for i in range(k):
                flag = 1
                for j in range(len(num)-1):
                    if num[j]>num[j+1]:
                        num = num[0:j]+num[j+1:]
                        flag = 0
                        break
                if flag == 1:
                    num = num[:-1]
            return str(int(num))