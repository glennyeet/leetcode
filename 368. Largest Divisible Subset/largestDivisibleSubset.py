from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Bottom-up DP: O(n^2) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        dp = [[num] for num in sorted_nums]
        max_subset = []
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if sorted_nums[j] % sorted_nums[i] == 0:
                    new_subset = [sorted_nums[i]] + dp[j]
                    if len(new_subset) > len(dp[i]):
                        dp[i] = new_subset
            if len(dp[i]) > len(max_subset):
                max_subset = dp[i]
        return max_subset
