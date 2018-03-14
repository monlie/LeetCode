class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for char in s[::-1]:
            if char == ' ' and length:
                break
            if char != ' ':
                length += 1
        return length
        