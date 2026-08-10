class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Bottom-up DP: O(n * √n) time, O(n) space

        dp = [False] * (n + 2)
        for i in range(n + 1):
            if not dp[i]:
                square_root_stones = 1
                while i + square_root_stones**2 <= n:
                    dp[i + square_root_stones**2] = True
                    square_root_stones += 1
        return dp[n]
