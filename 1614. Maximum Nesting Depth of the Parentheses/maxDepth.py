class Solution:
    def maxDepth(self, s: str) -> int:
        # Bracket Sequences: O(n) time, O(1) space,
        # where n is the size of s

        max_depth = 0
        cur_depth = 0
        for char in s:
            if char == "(":
                cur_depth += 1
            elif char == ")":
                max_depth = max(max_depth, cur_depth)
                cur_depth -= 1
        return max_depth
