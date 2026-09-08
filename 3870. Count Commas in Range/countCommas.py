class Solution:
    def countCommas(self, n: int) -> int:
        # Math: O(1) time, O(1) space

        return max(0, n - 1000 + 1)
