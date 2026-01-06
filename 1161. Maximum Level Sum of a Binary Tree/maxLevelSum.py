# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # BFS: O(n) time, O(n) space, where n is the number
        # of nodes in the binary tree rooted at root

        max_sum_level = 1
        max_level_sum = float("-inf")
        level = 1
        queue = deque([root])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > max_level_sum:
                max_sum_level = level
                max_level_sum = level_sum
            level += 1
        return max_sum_level
