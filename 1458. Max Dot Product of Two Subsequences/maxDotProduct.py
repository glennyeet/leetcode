from typing import List
from functools import cache


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        m = len(nums1)
        n = len(nums2)

        @cache
        def dp(i: int, j: int, non_empty: bool) -> int | float:
            if i == m or j == n:
                if non_empty:
                    return 0
                else:
                    return float("-inf")
            return max(
                nums1[i] * nums2[j] + dp(i + 1, j + 1, True),
                dp(i + 1, j, non_empty),
                dp(i, j + 1, non_empty),
            )

        return dp(0, 0, False)
