from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # Prefix Sum: O(n) time, O(1) space

        delta = 0
        min_delta = 0
        max_delta = 0
        for difference in differences:
            delta += difference
            min_delta = min(min_delta, delta)
            max_delta = max(max_delta, delta)
        max_difference = max_delta - min_delta
        return max(0, upper - (lower + max_difference) + 1)
