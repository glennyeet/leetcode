# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # DFS: O(n) time, O(n) space, where n is the number of nodes in the
        # binary tree rooted at root

        mod_factor = 10**9 + 7

        def find_tree_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return node.val + find_tree_sum(node.left) + find_tree_sum(node.right)

        tree_sum = find_tree_sum(root)
        max_sum_product = 0

        def find_max_product(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            subtree_sum = (
                node.val + find_max_product(node.left) + find_max_product(node.right)
            )
            nonlocal max_sum_product
            max_sum_product = max(
                max_sum_product, subtree_sum * (tree_sum - subtree_sum)
            )
            return subtree_sum

        find_max_product(root)

        return max_sum_product % mod_factor
