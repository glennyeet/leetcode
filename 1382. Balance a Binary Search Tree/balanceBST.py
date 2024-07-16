# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, node: TreeNode, nodes: List[TreeNode]):
        if not node:
            return
        self.inOrderTraversal(node.left, nodes)
        nodes.append(node)
        self.inOrderTraversal(node.right, nodes)

    def buildBalancedBST(self, nodes: List[TreeNode], start: int, end: int):
        if start > end:
            return
        mid = (start + end) // 2
        node = nodes[mid]
        node.left = self.buildBalancedBST(nodes, start, mid - 1)
        node.right = self.buildBalancedBST(nodes, mid + 1, end)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inOrderTraversal(root, nodes)
        return self.buildBalancedBST(nodes, 0, len(nodes) - 1)
