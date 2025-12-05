from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Prefix Sum: O(n) time, O(1) space

        n = len(nums)
        total_sum = sum(nums)
        cur_sum = 0
        valid_parititons = 0
        for i in range(n - 1):
            cur_sum += nums[i]
            valid_parititons += abs(total_sum - cur_sum - cur_sum) % 2 == 0
        return valid_parititons
