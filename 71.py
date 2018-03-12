class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        s = ''
        
        def put_path(stack, path):
            if path == '..' and stack:
                stack.pop()
            if path != '.' and path != '..':
                stack.append(path)
                
                
        for i in range(len(path)):
            if path[i] == '/' and s:
                put_path(stack, s)
                s = ''
                continue
            if path[i] == '/':
                continue
            s += path[i]
        
        if s:
            put_path(stack, s)
        
        return '/'+'/'.join(stack)