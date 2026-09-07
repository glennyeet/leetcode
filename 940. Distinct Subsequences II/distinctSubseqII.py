from functools import cache


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # Top-down DP: O(n^2) time, O(n) space

        mod_factor = 10**9 + 7
        n = len(s)

        @cache
        def dp(i: int) -> int:
            if i == n:
                return 1
            distinct_subsequences = 2 * dp(i + 1)
            for j in range(i + 1, n):
                if s[j] == s[i]:
                    distinct_subsequences -= dp(j + 1)
                    break
            return distinct_subsequences % mod_factor

        return (dp(0) - 1) % mod_factor
