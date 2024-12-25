# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from math import inf


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS: O(n) time, O(n) space
        max_row_values = []
        if not root:
            return max_row_values
        queue = deque([root])
        while queue:
            max_value = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_row_values.append(max_value)
        return max_row_values
