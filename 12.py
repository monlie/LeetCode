class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        
        def bar(x, up, mid, down):
            n = x - 5
            if n < -1:
                return x*down
            if n > 3:
                return down+up
            else:
                m = abs(n)
                return m*down + mid if m!= n else mid + m*down
            
        l = [num%(i*10)//i for i in [10**k for k in range(4)]][::-1]
        print(l)
        result = l[0] * 'M'
        for i in range(1, 4):
            result += bar(l[i], roman[2*i-2], roman[2*i-1], roman[2*i])
        return result
        