class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # Bottom-up DP + Prefix Sum: O(n * m) time, O(n)
        # space

        mod_factor = 10**9 + 7
        m = r - l + 1
        dp = [1] * m
        for _ in range(2, n + 1):
            dp.reverse()
            prefix_sum = 0
            for i in range(m):
                dp[i], prefix_sum = prefix_sum, (prefix_sum + dp[i]) % mod_factor
        return (sum(dp) * 2) % mod_factor
