from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Bottom-up DP: O(m^2 * n) time, O(m) space

        n = len(strs)
        m = len(strs[0])
        dp = [0] * (m + 1)
        for i in reversed(range(m)):
            dp[i] = 1
            for j in range(i + 1, m):
                for k in range(n):
                    if strs[k][i] > strs[k][j]:
                        break
                else:
                    dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)
