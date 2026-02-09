from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS + Divide and Conquer: O(n) time, O(n) space, where n is the
        # size of the tree rooted at root

        nodes = []

        def get_nodes(node: Optional[TreeNode]) -> None:
            if not node:
                return
            get_nodes(node.left)
            nodes.append(node)
            get_nodes(node.right)

        get_nodes(root)

        def build_balanced_tree(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = build_balanced_tree(start, mid - 1)
            node.right = build_balanced_tree(mid + 1, end)
            return node

        return build_balanced_tree(0, len(nodes) - 1)
