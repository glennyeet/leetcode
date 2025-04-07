from typing import List
# from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Top-down DP: O(n * sum(nums)) time, O(n * sum(nums)) space

        # n = len(nums)
        # nums_sum = sum(nums)
        # if nums_sum % 2:
        #     return False
        # max_subset_sum = nums_sum // 2

        # @cache
        # def is_equal_subset_possible(index: int, subset_sum: int) -> bool:
        #     if index == n or subset_sum > max_subset_sum:
        #         return False
        #     elif subset_sum == max_subset_sum:
        #         return True
        #     return is_equal_subset_possible(
        #         index + 1, subset_sum + nums[index]
        #     ) or is_equal_subset_possible(index + 1, subset_sum)

        # return is_equal_subset_possible(0, 0)

        # Bottom-up DP: O(n * sum(nums)) time, O(sum(nums)) space,
        # where n is the size of nums

        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        max_subset_sum = nums_sum // 2
        dp = [False] * (max_subset_sum + 1)
        dp[0] = True
        for num in nums:
            for i in reversed(range(num, len(dp))):
                if dp[i]:
                    continue
                elif dp[i - num]:
                    dp[i] = True
                if dp[max_subset_sum]:
                    return True
        return False
