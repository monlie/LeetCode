from math import factorial
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        lis = []
        k -= 1
        f = factorial(n)

        for i in range(2, n+1)[::-1]:
            f= f//i
            lis.append(k//f)
            k = k%f
            
        nums = list(range(n))
        result = ''
        
        for i in lis:
            num = nums.pop(i) + 1
            result += str(num)
        
        result += str(nums[0] + 1)
        
        return result
        
        