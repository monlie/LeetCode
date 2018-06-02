def is_codable(s):
    if s[0] == '0':
        return False
    return 1 <= int(s) <= 26



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        lis = [0] * len(s)
        lis[0] = 1
        last = 1
        for i in range(1, len(s)):
            if s[i] == "0" and not is_codable(s[i-1: i+1]):
                return 0
            a = 0
            if is_codable(s[i-1: i+1]) and is_codable(s[i]):
                lis[i] = lis[i-1] + (lis[i-2] if i-2 >= 0 else 1)
                last = 2
            elif s[i] == "0" and last == 2:
                lis[i] = lis[i-2] if i-2 >= 0 else 1
                last = 1
            else:
                lis[i] = lis[i-1]
                last = 1
                
            
        return lis[-1]
        
