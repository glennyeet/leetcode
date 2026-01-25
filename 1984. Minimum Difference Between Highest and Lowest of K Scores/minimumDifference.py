from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n * log(n)) time, O(n) space

        n = len(nums)
        sorted_scores = sorted(nums)
        min_difference = float("inf")
        for i in range(n - k + 1):
            min_difference = min(
                min_difference, sorted_scores[i + k - 1] - sorted_scores[i]
            )
        return min_difference
