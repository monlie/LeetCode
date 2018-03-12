class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        lis = [0] * len(nums)
        lis[0] = 1
        for n, i in enumerate(nums):
            if n == 0:
                continue
            m = 0
            for j in range(n):
                if nums[j] < i and lis[j] > m:
                    m = lis[j]          
            lis[n] = 1 + m
        return max(lis)