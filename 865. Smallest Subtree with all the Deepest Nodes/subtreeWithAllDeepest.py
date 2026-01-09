# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS: O(n) time, O(n) space, where n is the number of nodes in the binary
        # tree rooted at root

        def dfs(node: Optional[TreeNode]) -> tuple[Optional[TreeNode], int]:
            if not node:
                return None, 0
            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_subtree, left_depth + 1
            elif left_depth < right_depth:
                return right_subtree, right_depth + 1
            else:
                return node, left_depth + 1

        return dfs(root)[0]
