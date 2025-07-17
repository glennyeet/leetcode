from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Bottom-up DP: O(kn) time, O(k) space, where n is
        # the size of nums

        max_length = 0
        for target_remainder in range(k):
            dp = [0] * k
            for num in nums:
                cur_remainder = num % k
                dp[cur_remainder] = dp[(target_remainder - cur_remainder + k) % k] + 1
            max_length = max(max_length, max(dp))
        return max_length
