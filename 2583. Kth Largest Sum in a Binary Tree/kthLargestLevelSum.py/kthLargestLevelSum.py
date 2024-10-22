# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from heapq import heappush, heappushpop


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        level_sums = []
        while queue:
            level_size = len(queue)
            level_sum = 0
            while level_size > 0:
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
            if len(level_sums) < k:
                heappush(level_sums, level_sum)
            else:
                heappushpop(level_sums, level_sum)
        if len(level_sums) < k:
            return -1
        return level_sums[0]
