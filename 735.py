class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        def choose(a, b):
            return a if abs(a) > abs(b) else b
        
        
        def my_push(x, stack):
            if stack:
                top = stack.pop()
                if x < 0 and top > 0:
                    if top + x:
                        my_push(choose(x, top), stack)
                else:
                    stack.append(top)
                    stack.append(x)
                return
            stack.append(x)
            
        for i in asteroids:
            my_push(i, stack)
            
        return stack