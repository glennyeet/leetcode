from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
# Comment out when submitting in LeetCode.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(lambda: [0, 0])
        parents = set()
        for parent, child, is_left in descriptions:
            nodes[parent][1 - is_left] = child
            parents.add(parent)
        for _, child, _ in descriptions:
            parents.discard(child)
        root = TreeNode(list(parents)[0])

        def build(root: Optional[TreeNode]) -> None:
            left_child = nodes[root.val][0]
            if left_child:
                root.left = TreeNode(left_child)
                build(root.left)
            right_child = nodes[root.val][1]
            if right_child:
                root.right = TreeNode(right_child)
                build(root.right)

        build(root)
        return root
