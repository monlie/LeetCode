import numpy as np
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        lis = np.zeros((h, w), dtype=np.int32)
        lis[0, 0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(h):
            for j in range(w):
                if i == j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    lis[i, j] = 0
                    continue
                u = lis[i-1, j] if i-1 >= 0 else 0
                l = lis[i, j-1] if j-1 >= 0 else 0
                lis[i][j] = u+l
        return int(lis[-1, -1])