# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # DFS: O(n) time, O(n) space, where n is
        # is the number of nodes

        def decontaminate_tree(node: Optional[TreeNode]):
            x = node.val
            if node.left:
                node.left.val = 2 * x + 1
                decontaminate_tree(node.left)
            if node.right:
                node.right.val = 2 * x + 2
                decontaminate_tree(node.right)

        self.root = root
        self.root.val = 0
        decontaminate_tree(self.root)

    def find(self, target: int) -> bool:
        # DFS: O(n) time, O(n) space, where n is
        # is the number of nodes

        def search_tree(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if node.val == target:
                return True
            return search_tree(node.left) or search_tree(node.right)

        return search_tree(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
