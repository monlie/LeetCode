class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s = 0
        for n, i in enumerate(num1[::-1]):
            for m, j in enumerate(num2[::-1]):
                s += int(i)*10**n * int(j)*10**m
        return str(s)
        
