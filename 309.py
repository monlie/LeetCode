class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        lis = [0]*(n+1)
        lis[0] = -prices[0]
        al = [0]*n  # 此题中al长度是2就够了，我图省事这么写
        mark = 0
        
        for i in range(1, n):
            lis[i] = (al[i-2] - prices[i]) if mark else (al[i-1] - prices[i])
            sell = (prices[i] + max(lis[:i])) if len(lis[:i]) else 0
            al[i] = max(al[i-1], sell)
            if sell > al[i-1]:
                mark = 1
                
        return al[n-1]