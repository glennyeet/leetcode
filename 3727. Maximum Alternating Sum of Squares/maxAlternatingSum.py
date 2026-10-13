from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space

        n = len(nums)
        squared_nums = [num**2 for num in nums]
        squared_nums.sort()
        max_score = -sum(squared_nums[: n // 2]) + sum(squared_nums[n // 2 :])
        return max_score
