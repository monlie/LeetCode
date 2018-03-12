class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        d = [2, 3, 5]
        while 1:
            f = num
            for i in d:
                if num % i == 0:
                    num = num//i
            if f == num:
                break
        return num == 1
        