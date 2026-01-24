from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        max_pair_sum = 0
        for i in range(n // 2):
            max_pair_sum = max(max_pair_sum, sorted_nums[i] + sorted_nums[n - 1 - i])
        return max_pair_sum
