from functools import lru_cache


@lru_cache()
def rcr_brac(n):
    s = set()
    if n == 1:
        s.add('()')
        return s
        
    for m in range(1, n):
        for i in rcr_brac(m):
            if m == n - 1:
                s.add('(%s)' % i)
            for j in rcr_brac(n-m):
                s.add(i + j)
    return s


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(rcr_brac(n))
