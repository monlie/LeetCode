class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        m = 0
        last = 0
        l = len(s)
        for i in range(l):
            if s[i] not in d:
                last += 1
            elif i - d[s[i]] - 1 > last:
                last += 1
            else:
                last = i - d[s[i]]
            d[s[i]] = i
            if last > m:
                m = last
        
        return m
        
