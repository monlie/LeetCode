import numpy as np
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = np.zeros((n+1, n), dtype=np.int)
        lis[:, 0] = range(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                m = 0
                for k in range(1, i):
                    cur = k * lis[i-k, j-1]
                    if cur > m:
                        m = cur
                lis[i, j] = m
        return int(max(lis[n, 1:]))