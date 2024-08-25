# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []

        def traverse_tree(root: Optional[TreeNode]):
            if root == None:
                return
            traverse_tree(root.left)
            traverse_tree(root.right)
            traversal.append(root.val)
            return

        traverse_tree(root)
        return traversal
