class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lis = [0]*len(nums)
        lis[0] = nums[0]
        for i in range(1, len(nums)):
            past = max(lis[: i-1]) if i-1 > 0 else 0
            lis[i] = nums[i] + past
        return max(lis)