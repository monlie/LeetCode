class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        add = lambda a, b: a+b
        minus = lambda a, b: a-b
        op = {'+': add, '-': minus}
        dig = set(str(d) for d in range(10))
        stack = []
        post = ''
        num = ''
        for char in s:
            if char == ' ':
                continue
            if char in dig:
                num += char
                continue
            post += num + ' '
            num = ''
            if char == '(':
                stack.append(char)
            if char == ')':
                top = stack.pop()
                while top != '(':
                    post += top
                    top = stack.pop()
            if char in op:
                while stack and stack[-1] != '(':
                    post += stack.pop()
                stack.append(char)
        post += num + ' '
        while stack:
            post += stack.pop()
        
        num = ''
        for char in post:
            if char == ' ' and num:
                stack.append(int(num))
                num = ''
            if char in dig:
                num += char
            if char in op:
                a = stack.pop()
                b = stack.pop()
                stack.append(op[char](b, a))
        
        return stack.pop()
        