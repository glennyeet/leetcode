from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        # DFS: O(n) time, O(n) space

        n = len(preorder)
        postorder_val_to_index = {}
        for i, val in enumerate(postorder):
            postorder_val_to_index[val] = i

        def build_binary_tree(
            pre_left: int, pre_right: int, post_left: int
        ) -> Optional[TreeNode]:
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            if pre_left != pre_right:
                left_val = preorder[pre_left + 1]
                left_index = postorder_val_to_index[left_val]
                left_subtree_size = left_index - post_left + 1
                root.left = build_binary_tree(
                    pre_left + 1, pre_left + left_subtree_size, post_left
                )
                root.right = build_binary_tree(
                    pre_left + left_subtree_size + 1, pre_right, left_index + 1
                )
            return root

        return build_binary_tree(0, n - 1, 0)
