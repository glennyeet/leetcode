from collections import defaultdict


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        adj_list = defaultdict(list)
        for i in range(n):
            for word in dictionary:
                word_len = len(word)
                if s[i : i + word_len] == word:
                    adj_list[i].append(word_len)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(n):
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)
            for word_len in adj_list[i]:
                dp[i + word_len] = min(dp[i + word_len], dp[i])
        return dp[n]
