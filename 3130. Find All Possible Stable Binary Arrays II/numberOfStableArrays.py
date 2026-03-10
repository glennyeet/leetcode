class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Bottom-up DP: O(z * o) time, O(z * o) space, where z is zero and
        # o is one

        mod_factor = 10**9 + 7
        dp = [[[0, 0] * 3 for _ in range(one + 1)] for _ in range(zero + 1)]
        for i in range(zero + 1):
            if i <= limit:
                dp[i][0] = [1, 0]
            else:
                dp[i][0] = [0, 0]
        for j in range(one + 1):
            if j <= limit:
                dp[0][j] = [0, 1]
            else:
                dp[0][j] = [0, 0]
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp[i][j] = [sum(dp[i - 1][j]), sum(dp[i][j - 1])]
                if i > limit:
                    dp[i][j][0] -= dp[i - limit - 1][j][1]
                if j > limit:
                    dp[i][j][1] -= dp[i][j - limit - 1][0]
                for k in range(2):
                    dp[i][j][k] %= mod_factor
        return sum(dp[-1][-1]) % mod_factor
