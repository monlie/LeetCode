class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [0]*len(nums)
        m[0] = nums[0]
        for n, i in enumerate(nums):
            if n:
                m[n] = i if m[n-1] < 0 else i + m[n-1]
        return max(m)
            