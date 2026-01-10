from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        m = len(s1)
        n = len(s2)

        @cache
        def dp(i: int, j: int) -> int:
            if i == m and j == n:
                return 0
            elif i == m:
                return dp(i, j + 1) + ord(s2[j])
            elif j == n:
                return dp(i + 1, j) + ord(s1[i])
            min_ascii_sum = float("inf")
            if s1[i] == s2[j]:
                min_ascii_sum = dp(i + 1, j + 1)
            min_ascii_sum = min(
                min_ascii_sum, dp(i, j + 1) + ord(s2[j]), dp(i + 1, j) + ord(s1[i])
            )
            return min_ascii_sum

        return dp(0, 0)
