class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        l = len(height)
        lp = 0
        rp = l-1
        while lp != rp:
            s = min(height[lp], height[rp]) * (rp-lp)
            if s > m:
                m = s
            if height[lp] <= height[rp]:
                lp += 1
            else:
                rp -= 1
        return m
