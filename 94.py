# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        stack = []
        pr = root
        
        while stack or pr:
            while pr:
                stack.append(pr)
                pr = pr.left
            pr = stack.pop()
            l.append(pr.val)
            pr = pr.right
        return l