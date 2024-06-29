# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None or root.left is None and root.right is None:
            return
        if root.left is not None:
            self.flatten(root.left)
            temp = root.right
            root.right = root.left
            root.left = None
            while root.right is not None:
                root = root.right
            root.right = temp
        self.flatten(root.right)