# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node_heights = {}

        def get_heights(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            height = max(get_heights(node.left), get_heights(node.right))
            node_heights[node.val] = height
            return height + 1

        get_heights(root)
        max_depths = [0] * (len(node_heights) + 1)

        def get_max_depths(node: Optional[TreeNode], depth: int, max_depth: int):
            if not node:
                return
            left_height = depth
            right_height = depth
            max_depths[node.val] = max_depth
            if node.right:
                right_height += 1 + node_heights[node.right.val]
            get_max_depths(node.left, depth + 1, max(max_depth, right_height))
            if node.left:
                left_height += 1 + node_heights[node.left.val]
            get_max_depths(node.right, depth + 1, max(max_depth, left_height))

        get_max_depths(root, 0, 0)
        answer = []
        for query in queries:
            answer.append(max_depths[query])
        return answer
