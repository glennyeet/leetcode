from typing import List
from functools import cache


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # Top-down DP: O(n^2) time, O(n) space

        n = len(nums)

        @cache
        def get_max_jumps(i: int) -> int:
            if i == n - 1:
                return 0
            max_jumps = 0
            has_jump = False
            for j in range(i + 1, n):
                if abs(nums[j] - nums[i]) <= target:
                    remaining_jumps = get_max_jumps(j)
                    if remaining_jumps != -1:
                        has_jump = True
                        max_jumps = max(max_jumps, 1 + remaining_jumps)
            if not has_jump:
                return -1
            return max_jumps

        return get_max_jumps(0)
