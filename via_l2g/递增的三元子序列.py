class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = None
        second = None
        ext = None
        for x in nums:
            if ext is not None:
                if ext < x < second:
                    first, second = ext, x
                    ext = None
                    continue
            if first is None:
                first = x
            if second is not None:
                if x > second:
                    return True
                if first < x < second:
                    second = x
                if x < first:
                    ext = x
            else:
                if x <= first:
                    first = x
                else:
                    second = x
        return False
