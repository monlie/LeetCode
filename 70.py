class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = [0] * (n+1)
        lis[0] = 1
        lis[1] = 1
        for i in range(2, n+1):
            lis[i] = lis[i-1] + lis[i-2]
        return lis[-1]