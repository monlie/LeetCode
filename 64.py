import numpy as np
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        lis = np.zeros((h, w), dtype=np.int32)
        lis[0, 0] = grid[0][0]
        for i in range(h):
            for j in range(w):
                if i == j == 0:
                    continue
                u = lis[i-1, j] if i-1 >= 0 else 1e5
                l = lis[i, j-1] if j-1 >= 0 else 1e5
                lis[i, j] = grid[i][j] + min(u ,l)
        return int(lis[-1, -1])