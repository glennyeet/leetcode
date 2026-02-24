from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # DFS + Bit Manipulation: O(n) time, O(n) space, where
        # n is the size of the binary tree rooted at root

        tree_sum = 0

        def dfs(node: Optional[TreeNode], num: int) -> None:
            if not node:
                return
            if not node.left and not node.right:
                nonlocal tree_sum
                tree_sum += num
                return
            if node.left:
                dfs(node.left, num << 1 | node.left.val)
            if node.right:
                dfs(node.right, num << 1 | node.right.val)

        dfs(root, root.val)
        return tree_sum
