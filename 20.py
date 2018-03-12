class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')': '(',
             ']': '[',
             '}': '{'}
        stack = []
        for char in s:
            if char in d.values():
                stack.append(char)
            if char in d.keys():
                top = stack.pop() if stack else None
                if top != d[char]:
                    return False
        if stack:
            return False
        return True
        