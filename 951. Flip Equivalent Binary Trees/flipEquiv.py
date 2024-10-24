# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == root2 == None:
            return True
        elif not root1 and root2 or root1 and not root2 or root1.val != root2.val:
            return False

        def match_nodes(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 == node2 == None:
                return True
            if not node1 or not node2:
                return False
            if node1.val == node2.val:
                return (
                    match_nodes(node1.left, node2.left)
                    and match_nodes(node1.right, node2.right)
                    or match_nodes(node1.right, node2.left)
                    and match_nodes(node1.left, node2.right)
                )
            return False

        return (
            match_nodes(root1.left, root2.left)
            and match_nodes(root1.right, root2.right)
            or match_nodes(root1.left, root2.right)
            and match_nodes(root1.right, root2.left)
        )
