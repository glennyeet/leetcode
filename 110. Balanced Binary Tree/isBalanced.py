from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS: O(n) time, O(n) space, where n is the number of
        # nodes in the tree rooted at root

        is_height_balanced = True

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal is_height_balanced
            if not node or not is_height_balanced:
                return 0
            left_subtree_depth = dfs(node.left)
            right_subtree_depth = dfs(node.right)
            if abs(left_subtree_depth - right_subtree_depth) > 1:
                is_height_balanced = False
            return 1 + max(left_subtree_depth, right_subtree_depth)

        dfs(root)
        return is_height_balanced
