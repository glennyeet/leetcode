from math import ceil, floor


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Math: O(1) time, O(1) space

        return ceil(high / 2) - floor(low / 2)
