from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # Prefix Sum: O(n) time, O(k) space, where n is the
        # size of nums

        prefix_sum = [float("inf")] * k
        prefix_sum[0] = 0
        max_sum = float("-inf")
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            prefix_len = (i + 1) % k
            max_sum = max(max_sum, cur_sum - prefix_sum[prefix_len])
            prefix_sum[prefix_len] = min(prefix_sum[prefix_len], cur_sum)
        return max_sum
