"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursive
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if root is None:
            return []
        elif len(root.children) == 0:
            return [root.val]
        values = self.postorder(root.children[0])
        for i in range(1, len(root.children)):
            values += self.postorder(root.children[i])
        values += [root.val]
        return values

# Iterative
# class Solution:
#     def postorder(self, root: "Node") -> List[int]:
#         values = []
#         stack = []
#         if root is not None:
#             stack.append([root, 0]) # node, latest child finished processing (0 means none)
#         while len(stack) > 0:
#             node, index = stack[-1]
#             if index < len(node.children):
#                 stack[-1][1] += 1
#                 stack.append([node.children[index], 0])
#             else:
#                 stack.pop()
#                 values.append(node.val)
#         return values


# Recursive #2
# class Solution:
#     def postorder(self, root: "Node") -> List[int]:
#         values = []
#         if not root:
#             return values
#         for child in root.children:
#             values += self.postorder(child)
#         values.append(root.val)
#         return values
