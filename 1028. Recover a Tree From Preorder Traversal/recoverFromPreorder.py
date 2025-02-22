from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Stack: O(n) time, O(n) space

        n = len(traversal)
        i = 0
        stack: list[Optional[TreeNode]] = []
        dashes = 0
        while i < n:
            if traversal[i] == "-":
                dashes += 1
                i += 1
            else:
                j = i
                while j < n and traversal[j] != "-":
                    j += 1
                node = TreeNode(int(traversal[i:j]))
                while len(stack) > dashes:
                    stack.pop()
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                stack.append(node)
                dashes = 0
                i = j
        return stack[0]
