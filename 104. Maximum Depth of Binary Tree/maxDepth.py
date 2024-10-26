# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            height = 1 + max(get_height(node.left), get_height(node.right))
            return height

        return get_height(root)
