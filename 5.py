# 这题我做法略清奇，虽然ac了，但是值得仔细思考
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lis = [[] for _ in range(n)]
        lis[0] = [0, 0]
        for i, char in enumerate(s):
            if i == 0:
                continue
            lis[i].append(i)
            for m in lis[i-1]:
                if i-1 == m:
                    continue
                if s[i-2-m] == char:
                    lis[i].append(m+2)
            if char == s[i-1]:
                lis[i].append(1)
            lis[i].append(0)
        idx, l = max(lis, key=lambda x: x[1])[:2]
        return s[idx-l: idx+1]
                
        