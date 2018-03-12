# 注意：这份代码并没有ac（笑
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = [0]*n
        num = [2, 3, 5]
        lis[:5] = [1, 2, 3, 4, 5]
        for i in range(5, n):
            m = 2*lis[i-1]
            for p in lis[:i][::-1]:
                if p*5 <= lis[i-1]:
                    break
                for j in num:
                    k = j*p
                    if k >= m:
                        break
                    if k > lis[i-1]:
                        m = k
            lis[i] = m
        return lis[n-1]