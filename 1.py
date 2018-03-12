class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def bi_find(nums, n):
            l = len(nums)
            if l == 0:
                return []
            cut = l//2 - 1
            cut = cut if cut > 0 else 0
            c = nums[cut]
            if n == c[1]:
                if l > 1 and nums[cut+1][1] == n:
                    return [c[0], nums[cut+1][0]]
                return [c[0]]
            if n > c[1]:
                return bi_find(nums[cut+1:], n)
            if n < c[1]:
                return bi_find(nums[:cut], n)
        
        sort_ = sorted(enumerate(nums), key=lambda k: k[1])
            
        minus = [target-i for i in nums]
        for i, n in enumerate(minus):
            idxs = bi_find(sort_, n)
            if idxs:
                for j in idxs:
                    if i != j:
                        return [i, j]