# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_children(node: Optional[TreeNode]):
            if not node:
                return
            node.left, node.right = node.right, node.left
            if node.left:
                swap_children(node.left)
            if node.right:
                swap_children(node.right)

        swap_children(root)
        return root
