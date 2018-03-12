from functools import reduce
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d = {2: 'abc',
             3: 'def',
             4: 'ghi',
             5: 'jkl',
             6: 'mno',
             7: 'pqrs',
             8: 'tuv',
             9: 'wxyz'}
        def combine(l, r):
            p = []
            for u in l:
                for char in r:
                    p.append(u + char)
            return p
        dig = [d[int(i)] for i in digits]
        return list(reduce(combine, dig))
        