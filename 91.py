class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_decode(n):
            n = int(n) if int(n[0]) else 0
            return 0 < n < 27
        
        if not s:
            return 0
        lis = [0]*len(s)
        lis[0] = 1 if is_decode(s[0]) else 0
        for n, char in enumerate(s):
            if not n:
                continue
            single = lis[n-1] if is_decode(char) else 0
            double = (lis[n-2] if n-2 >= 0 else 1) if is_decode(s[n-1: n+1]) else 0
            lis[n] = single + double
            
        return lis[-1]
        