import numpy as np
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = np.zeros((len(nums), 2), dtype=np.int)
        lis[0, :] = nums[0]
        for i in range(1, len(nums)):
            last_min = lis[i-1][0]*nums[i]
            last_max = lis[i-1][1]*nums[i]
            min_ = min(nums[i], last_min, last_max)
            max_ = max(nums[i], last_min, last_max)
            lis[i, :] = [min_, max_]
        return int(max(lis[:, 1]))
        