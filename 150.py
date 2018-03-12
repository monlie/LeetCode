class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        d = {'+': (lambda a, b: a+b),
             '-': (lambda a, b: a-b),
             '*': (lambda a, b: a*b),
             '/': (lambda a, b: int(a/b))}
        
        stack = []
        
        for e in tokens:
            if e in d:
                a = stack.pop()
                b = stack.pop()
                v = d[e](b, a)
                print(v)
                stack.append(v)
            else:
                stack.append(int(e))

        return stack.pop()
        