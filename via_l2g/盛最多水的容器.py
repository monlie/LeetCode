class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        left = 0
        right = len(height) - 1
        s = right - left
        
        while left < right:
            if height[left] < height[right]:
                cur = height[left] * s
                left += 1
            else:
                cur = height[right] * s
                right -= 1
            
            if cur > m:
                m = cur
            
            s -= 1
            
        return m
        
