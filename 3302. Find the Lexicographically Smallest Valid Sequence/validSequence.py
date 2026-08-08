from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        # Bottom-up DP + Greedy: O(m + n) time, O(m + n) space

        n = len(word1)
        m = len(word2)
        dp = [-1] * (m + 1)
        dp[m] = n
        r = n - 1
        for i in reversed(range(m)):
            while r >= 0 and word1[r] != word2[i]:
                r -= 1
            dp[i] = r
            if r < 0:
                break
            r -= 1
        ans = []
        used = False
        r = 0
        for i in range(n):
            if r >= m:
                break
            if word1[i] == word2[r]:
                ans.append(i)
                r += 1
                continue
            if not used and dp[r + 1] >= i + 1:
                ans.append(i)
                used = True
                r += 1
                continue
        if len(ans) != m:
            return []
        return ans
