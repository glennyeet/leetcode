# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, root.val)])
        while queue:
            depth_sum = 0
            for node, _ in queue:
                depth_sum += node.val
            depth_nodes = len(queue)
            while depth_nodes > 0:
                depth_nodes -= 1
                node, non_cousin_sum = queue.popleft()
                node.val = depth_sum - non_cousin_sum
                if node.left:
                    non_cousin_sum = node.left.val
                    if node.right:
                        non_cousin_sum += node.right.val
                    queue.append((node.left, non_cousin_sum))
                if node.right:
                    non_cousin_sum = node.right.val
                    if node.left:
                        non_cousin_sum += node.left.val
                    queue.append((node.right, non_cousin_sum))
        return root
