class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'M': 1000,
             'D': 500,
             'C': 100,
             'L': 50,
             'X': 10,
             'V': 5,
             'I': 1}
        
        def roman_iter(s):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return d[s[0]]
            f = d[s[0]]
            n = d[s[1]]
            if n < f:
                return f + roman_iter(s[1:])
            if n > f:
                return n-f+roman_iter(s[2:])
            else:
                for pos in range(2, len(s)):
                    if d[s[pos]] > f:
                        return d[s[pos]]-pos*f+roman_iter(s[pos+1:])
                    if d[s[pos]] < f:
                        return pos*f+roman_iter(s[pos:])
                return len(s)*f
        return roman_iter(s)
                