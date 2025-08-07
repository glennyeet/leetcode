from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # Bottom-up DP: O(n^2) time, O(n^2) space

        n = len(fruits)
        diagonal = 0
        formatted_fruits = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                formatted_fruits[i][j] = fruits[i][j]
        for i in range(n):
            diagonal += formatted_fruits[i][i]
            formatted_fruits[i][i] = float("-inf")
        formatted_fruits[n - 1][n - 1] = 0
        dp = [[float("-inf")] * n for _ in range(n)]
        dp[0][n - 1] = formatted_fruits[0][n - 1]
        for i in range(1, n):
            for j in range(n):
                for dj in [-1, 0, 1]:
                    if 0 <= j + dj < n:
                        dp[i][j] = max(
                            dp[i - 1][j + dj] + formatted_fruits[i][j], dp[i][j]
                        )
        best_tr = dp[n - 1][n - 1]
        dp = [[float("-inf")] * n for _ in range(n)]
        dp[n - 1][0] = formatted_fruits[n - 1][0]
        for j in range(1, n):
            for i in range(n):
                for di in [-1, 0, 1]:
                    if 0 <= i + di < n:
                        dp[i][j] = max(
                            dp[i + di][j - 1] + formatted_fruits[i][j], dp[i][j]
                        )
        best_bl = dp[n - 1][n - 1]

        return diagonal + best_tr + best_bl
