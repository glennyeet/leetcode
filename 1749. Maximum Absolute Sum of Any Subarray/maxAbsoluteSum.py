from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Prefix sum: O(n) time, O(1) space

        prefix_sum = 0
        max_abs_sum = 0
        min_sum = float("inf")
        max_sum = float("-inf")
        for num in nums:
            prefix_sum += num
            min_sum = min(min_sum, prefix_sum)
            max_sum = max(max_sum, prefix_sum)
            max_abs_sum = max(
                max_abs_sum,
                abs(prefix_sum),
                abs(prefix_sum - min_sum),
                abs(prefix_sum - max_sum),
            )
        return max_abs_sum
