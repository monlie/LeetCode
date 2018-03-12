import numpy as np
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = set(range(n))
        count = 0
        
        def get_poss(mat, pos):
            cur = s-set(mat[:pos])
            dig = set()
            for k, p in enumerate(mat[:pos]):
                l = p-(pos-k)
                r = p+(pos-k)
                if 0 <= l < n:
                    dig.add(l)
                if 0 <= r < n:
                    dig.add(r)
            return list(cur-dig)
        
        
        def solve(mat, k):
            nonlocal count
            if not k:
                count += 1
            cur = n-k
            l = get_poss(mat, cur)
            for pos in l:
                new = mat.copy()
                new[cur] = pos
                solve(new, k-1)
                
        h = np.zeros((n, ), dtype=np.int)
        solve(h, n)
        
        return count