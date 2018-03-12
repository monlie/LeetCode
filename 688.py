import numpy as np
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        
        def is_inside(i, j):
            return 0 <= i < N and 0 <= j < N
        
        lis = np.zeros((N, N, K+1), dtype=np.float64)
        lis[:, :, 0] = 1
        for k in range(1, K+1):
            for i in range(N):
                for j in range(N):
                    lis[i, j, k] = (((lis[i+2, j+1, k-1] if is_inside(i+2, j+1) else 0)+
                                     (lis[i+2, j-1, k-1] if is_inside(i+2, j-1) else 0)+
                                     (lis[i-2, j+1, k-1] if is_inside(i-2, j+1) else 0)+
                                     (lis[i-2, j-1, k-1] if is_inside(i-2, j-1) else 0)+
                                     (lis[i+1, j+2, k-1] if is_inside(i+1, j+2) else 0)+
                                     (lis[i-1, j+2, k-1] if is_inside(i-1, j+2) else 0)+
                                     (lis[i+1, j-2, k-1] if is_inside(i+1, j-2) else 0)+
                                     (lis[i-1, j-2, k-1] if is_inside(i-1, j-2) else 0))/8)
        return float(lis[c, r, K])