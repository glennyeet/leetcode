from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Prefix Sum: O(n) time, O(n) space

        n = len(nums)
        strictly_increasing_lengths = [1] * n
        streak = 0
        for i in reversed(range(n)):
            if i == n - 1 or i < n - 1 and nums[i] < nums[i + 1]:
                streak += 1
                strictly_increasing_lengths[i] = streak
            else:
                streak = 1
                strictly_increasing_lengths[i] = streak
        for i in range(0, n - k):
            if (
                strictly_increasing_lengths[i] >= k
                and strictly_increasing_lengths[i + k] >= k
            ):
                return True
        return False
