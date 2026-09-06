from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Top-down DP: O(m * n) time, O(m * n) space

        n = len(s)
        m = len(t)

        @cache
        def dp(s_index: int, t_index: 0) -> int:
            if t_index == m:
                return 1
            elif s_index == n:
                return 0
            subsequences = 0
            if s[s_index] == t[t_index]:
                subsequences += dp(s_index + 1, t_index + 1)
            subsequences += dp(s_index + 1, t_index)
            return subsequences

        return dp(0, 0)
