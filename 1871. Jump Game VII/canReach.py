class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Bottom-up DP + Sliding Window: O(n) time, O(n) space

        n = len(s)
        dp = [False] * n
        dp[0] = True
        total_i = 0
        for j in range(n):
            if j - minJump >= 0 and dp[j - minJump]:
                total_i += 1
            if j - maxJump - 1 >= 0 and dp[j - maxJump - 1]:
                total_i -= 1
            if s[j] == "0" and total_i > 0:
                dp[j] = True
        return dp[-1]
