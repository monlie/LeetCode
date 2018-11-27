class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        
        down = 0
        while down < len(nums) and s[down] == nums[down]:
            down += 1
            
        up = len(nums) - 1
        while up >= down and s[up] == nums[up]:
            up -= 1
            
        return up - down + 1 if up != down else 0
