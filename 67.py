class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def half_adder(a, b):
            return a^b, a&b
        
        def full_adder(a, b, c_in):
            s, c_out = half_adder(a, b)
            s, c = half_adder(s, c_in)
            return s, c|c_out
        
        length = max(len(a), len(b)) + 1
        c = 0
        a = [int(a[::-1][i]) if i < len(a) else 0 for i in range(length)]
        b = [int(b[::-1][i]) if i < len(b) else 0 for i in range(length)]
        s = [0]*length

        for i in range(length):
            s[i], c = full_adder(a[i], b[i], c)
        
        s = s[::-1]
        pr = 0
        while s[pr: ] and not s[pr]:
            pr += 1
            
        if not s[pr: ]:
            return '0'
        
        result = ''
        for char in s[pr: ]:
            result += str(char)
        return result