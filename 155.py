class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            if x < self.min:
                self.min = x
        else:
            self.min = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.min:
            self.min = min(self.stack) if self.stack else 0
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()