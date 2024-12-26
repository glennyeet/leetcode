from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top-down DP: O(n * sum(nums)) time, O(n * sum(nums)) space

        # dp = {}

        # def find_total_expressions(index: int, cur_sum: int) -> int:
        #     if index == len(nums):
        #         return cur_sum == target
        #     elif (index, cur_sum) in dp:
        #         return dp[(index, cur_sum)]
        #     dp[(index, cur_sum)] = find_total_expressions(
        #         index + 1, cur_sum + nums[index]
        #     ) + find_total_expressions(index + 1, cur_sum - nums[index])
        #     return dp[(index, cur_sum)]

        # return find_total_expressions(0, 0)

        # Bottom-up DP: O(n * sum(nums)) time, O(n * sum(nums)) space

        # dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        # dp[0][0] = 1
        # for i, num in enumerate(nums):
        #     for cur_sum, expressions in dp[i].items():
        #         dp[i + 1][cur_sum + num] += expressions
        #         dp[i + 1][cur_sum - num] += expressions
        # return dp[len(nums)][target]

        # Bottom-up DP with optimized space: O(n * sum(nums)) time, O(sum(nums)) space

        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for cur_sum, expressions in dp.items():
                next_dp[cur_sum + num] += expressions
                next_dp[cur_sum - num] += expressions
            dp = next_dp
        return dp[target]
