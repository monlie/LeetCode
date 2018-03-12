import numpy as np
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        s = set(range(n))
        solve_list = []
        
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
        
        def translator(mat):
            s = len(mat)
            l = []
            for j in mat:
                c = ''
                for i in range(s):
                    c += '.' if i!= j else'Q'
                l.append(c)
            return l
        
        def solve(mat, k):
            if not k:
                solve_list.append(mat)
            cur = n-k
            l = get_poss(mat, cur)
            for pos in l:
                new = mat.copy()
                new[cur] = pos
                solve(new, k-1)
                
        h = np.zeros((n, ), dtype=np.int)
        solve(h, n)
        
        return list(map(translator, solve_list))