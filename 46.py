from copy import deepcopy

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute_iter(n):
            if n:
                last = permute_iter(n-1)
                p = nums[n]
                new = []
                for item in last:
                    for i in range(n+1):
                        d = deepcopy(item)
                        d.insert(i, p)
                        new.append(d)
                return new
            return [[nums[0]]]
        
        return permute_iter(len(nums)-1)