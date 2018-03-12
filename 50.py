class Solution:
    def myPow(self, y, m):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def pow_iter(x, n):
            if n == 0:
                return 1
            if n % 2 == 0:
                s = pow_iter(x, n//2)
                return s*s
            return x*pow_iter(x, n-1)
        
        abs_pow =  pow_iter(y, abs(m))
        return abs_pow if m >= 0 else 1/abs_pow
        