class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def nonzero(l):
            if not l:
                return []
            if l[-1]:
                return l
            return nonzero(l[:-1])
        s = 1 if x >= 0 else -1
        x = abs(x)
        t = []
        i = 0
        while x//10**i:
            t.append(x%(10**(i+1))//10**i)
            i += 1
        t = nonzero(t)
        
        r = 0
        for n, i in enumerate(t):
            r += i * 10**(len(t)-1-n)
            
        r = r if r < 2147483647 else 0
        return r * s