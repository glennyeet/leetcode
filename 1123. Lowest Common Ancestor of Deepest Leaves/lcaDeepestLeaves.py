from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS + DFS: O(n) time, O(n) space, where n is number of nodes

        queue = deque([root])
        while queue:
            deepest_leaves = []
            for _ in range(len(queue)):
                node = queue.popleft()
                deepest_leaves.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        def find_lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            elif node.val == deepest_leaves[0] or node.val == deepest_leaves[-1]:
                return node
            left_node = find_lca(node.left)
            right_node = find_lca(node.right)
            if left_node and right_node:
                return node
            return left_node or right_node

        return find_lca(root)
