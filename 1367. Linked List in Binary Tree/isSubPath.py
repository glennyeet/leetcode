# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def is_path(l_node: int, b_node: int) -> bool:
            if not l_node:
                return True
            if not b_node:
                return False
            if b_node.val == l_node.val:
                return is_path(l_node.next, b_node.left) or is_path(
                    l_node.next, b_node.right
                )
            return False

        def find_start_point(b_node: int) -> bool:
            if not b_node:
                return False
            path_found = False
            if b_node.val == head.val:
                path_found = is_path(head, b_node)
            return path_found or find_start_point(b_node.left) or find_start_point(b_node.right)

        return find_start_point(root)
