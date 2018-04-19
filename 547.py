def dfs(edge, i, visit):
    if i in visit:
        return
    visit.add(i)
    for n, j in enumerate(edge[i]):
        if n == i:
            continue
        if j == 1:
            dfs(edge, n, visit)

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visit = set()
        s = 0
        for i in range(len(M)):
            if i not in visit:
                s += 1
                dfs(M, i, visit)
        return s
        
        
