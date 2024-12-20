# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS, Time: O(n), Space: O(n)

        # nodes = deque([root])
        # level = 0
        # while nodes:
        #     if level & 1:
        #         l = 0
        #         r = len(nodes) - 1
        #         while l < r:
        #             nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
        #             l += 1
        #             r -= 1
        #     for _ in range(len(nodes)):
        #         node = nodes.popleft()
        #         if node.left:
        #             nodes.append(node.left)
        #         if node.right:
        #             nodes.append(node.right)
        #     level += 1
        # return root

        # DFS, Time: O(n), Space: O(log(n))

        def reverse_binary_tree(
            left_node: Optional[TreeNode], right_node: Optional[TreeNode], level: int
        ):
            if level & 1:
                left_node.val, right_node.val = right_node.val, left_node.val
            if left_node.left:
                reverse_binary_tree(left_node.left, right_node.right, level + 1)
                reverse_binary_tree(left_node.right, right_node.left, level + 1)

        if root.left:
            reverse_binary_tree(root.left, root.right, 1)
        return root
