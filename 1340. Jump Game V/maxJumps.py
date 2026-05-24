from typing import List
from functools import cache


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Top-down DP: O(n^2) time, O(n) space

        n = len(arr)

        @cache
        def dp(i: int) -> int:
            max_indices = 1
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] <= arr[j]:
                    break
                max_indices = max(max_indices, 1 + dp(j))
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[i] <= arr[j]:
                    break
                max_indices = max(max_indices, 1 + dp(j))
            return max_indices

        max_indices = 0
        for i in range(n):
            max_indices = max(max_indices, dp(i))
        return max_indices
