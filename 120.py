class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        d = len(triangle)
        lis = [[0]*d for _ in range(d)]
        lis[0][0] = triangle[0][0]
        for i in range(1, d):
            for j in range(i+1):
                l = lis[i-1][j-1] if j-1 >= 0 else 1e5
                r = lis[i-1][j] if j < i else 1e5
                lis[i][j] = min(l+triangle[i][j], r+triangle[i][j])
        return min(lis[d-1])