from math import floor


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # Binary Tree: O(n) time, O(n) space, where n is the size of the
        # binary tree rooted at root

        equal_subtree_average_nodes = 0

        def find_average(root: TreeNode) -> tuple[int, int]:
            value_sum = root.val
            values = 1
            if root.left:
                left_child_sum, left_child_nodes = find_average(root.left)
                value_sum += left_child_sum
                values += left_child_nodes
            if root.right:
                right_child_sum, right_child_nodes = find_average(root.right)
                value_sum += right_child_sum
                values += right_child_nodes
            value_average = floor(value_sum / values)
            if value_average == root.val:
                nonlocal equal_subtree_average_nodes
                equal_subtree_average_nodes += 1
            return value_sum, values

        find_average(root)
        return equal_subtree_average_nodes
