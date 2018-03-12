class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.b = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.a:
            self.a.append(x)
        else:
            self.b.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.a:
            for i in range(len(self.a)-1):
                self.b.append(self.a.pop())
            k = self.a.pop()
            for i in range(len(self.b)):
                self.a.append(self.b.pop())
            return k
            
        for i in range(len(self.b)-1):
            self.a.append((self.b.pop()))
        k = self.b.pop()
        for i in range(len(self.a)):
                self.b.append(self.a.pop())
        return k

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        print(self.a, self.b)
        if self.a:
            return self.a[0]
        return self.b[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        print(self.a, self.b)
        return not self.a and not self.b


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()