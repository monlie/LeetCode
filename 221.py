class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        lis = [[0]*w for _ in range(h)]
        lis[0][0] = int(matrix[0][0])
        for i in range(h):
            for j in range(w):
                if i == j == 0:
                    continue
                if matrix[i][j] == '0':
                    lis[i][j] = 0
                    continue
                k = lis[i-1][j-1] if i >= 0 and j >= 0 else 0
                u = lis[i-1][j] if i-1 >= 0 else 0
                l = lis[i][j-1] if j-1 >= 0 else 0
                lis[i][j] = 1+min(k, u, l)
        return max([max(row) for row in lis])**2