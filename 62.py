import numpy as np

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lis = np.zeros((m, n), dtype=np.int32)
        lis[:, 0] = 1
        lis[0, :] = 1
        for i in range(1, m):
            for j in range(1, n):
                lis[i, j] = lis[i-1, j] + lis[i, j-1]
        return int(lis[-1, -1])