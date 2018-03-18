class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """        
        lis = [[0] * len(coins) for _ in range(amount+1)]
        
        def judge(n , pr):
            if n >= 0 and pr >= 0:
                return lis[n][pr]
            return -1
        
        
        def poss_min(a, b):
            if a == -1:
                return b
            if b == -1 and a != -1:
                return a + 1
            return min(a + 1, b)
        
        for n in range(1, amount + 1):
            for pr in range(len(coins)):
                lis[n][pr] = poss_min(judge(n-coins[pr], pr), judge(n, pr-1))
                
        m = -1
        
        for i in lis[-1]:
            if i != -1 and (i < m or m == -1):
                m = i

        return m