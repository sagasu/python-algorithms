class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        temp = str.strip()
        if not temp:
            return 0
        negative = False
        resint = 0
        head = temp[0]
        if head == "-":
            negative = True
        elif head == "+":
            negative = False
        elif not head.isnumeric():
            return 0
        else:
            resint += ord(head) - ord('0')
        for i in range(1,len(temp)):
            if temp[i].isnumeric():
                resint = 10*resint + ord(temp[i]) - ord('0')
                if not negative and resint >= 2147483647:
                    return 2147483647
                if negative and resint >= 2147483648:
                    return -2147483648
            else:
                break
        if not negative:
            return resint
        else:
            return -resint