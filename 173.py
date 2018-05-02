# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def bst(root, l):
    if root:
        bst(root.left, l)
        l.append(root.val)
        bst(root.right, l)
    
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.l = []
        self.idx = 0
        bst(root, self.l)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.l)
        

    def next(self):
        """
        :rtype: int
        """
        val = self.l[self.idx]
        self.idx += 1
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
