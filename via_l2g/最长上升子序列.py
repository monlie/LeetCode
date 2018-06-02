def max_before(a, b, i):
    l = len(a)
    m = 0
    for j in range(l):
        if b[j] < i and a[j] > m:
            m = a[j]
    return m


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lis = [0] * len(nums)
        lis[0] = 1
        for i in range(1, len(nums)):
            lis[i] = max_before(lis[:i], nums[:i], nums[i]) + 1
        return max(lis)
        
