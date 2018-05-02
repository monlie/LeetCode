# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def is_valid_bst(root):
    if not root:
        return 1e10, -1e10, True
    rmin, rmax, rb = is_valid_bst(root.right)
    lmin, lmax, lb = is_valid_bst(root.left)
    return min(lmin, root.val), max(rmax, root.val), rb and lb and lmax < root.val < rmin
    
    
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        mi, ma, b = is_valid_bst(root)
        return b
