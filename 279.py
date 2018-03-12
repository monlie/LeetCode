from math import sqrt, floor
import numpy as np

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = np.zeros(n+1, dtype=np.int)
        
        for i in range(1, n+1):
            k = floor((sqrt(i)))
            if k*k == i:
                lis[i] = 1
                continue
            m = lis[i-1]
            for j in range(1, k):
                cur = lis[i-(j+1)**2]
                if cur < m:
                    m = cur
            lis[i] = 1 + m
        return int(lis[n])