# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        level_groups = []
        queue = deque([root])
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_groups.append(level_nodes)
        min_operations = 0
        for group in level_groups:
            num_indices = {}
            for i, num in enumerate(group):
                num_indices[num] = i
            sorted_group = sorted(group)
            for i, (num1, num2) in enumerate(zip(group, sorted_group)):
                if num1 != num2:
                    min_operations += 1
                    sorted_i = num_indices[num2]
                    group[i], group[sorted_i] = group[sorted_i], group[i]
                    num_indices[group[sorted_i]] = sorted_i
        return min_operations
