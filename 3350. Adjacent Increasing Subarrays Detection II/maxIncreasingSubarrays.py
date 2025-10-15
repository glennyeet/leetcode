from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # Sliding Window: O(n) time, O(1) space

        n = len(nums)
        streak = 0
        max_k = 0
        prev_subarray_start = 0
        cur_subarray_start = 0
        for i in range(n):
            if i == 0 or nums[i - 1] < nums[i]:
                streak += 1
            else:
                streak = 1
                prev_subarray_start = cur_subarray_start
                cur_subarray_start = i
            max_k = max(
                max_k,
                streak // 2,
                min(
                    cur_subarray_start - prev_subarray_start, i - cur_subarray_start + 1
                ),
            )
        return max_k
