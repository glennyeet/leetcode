from itertools import groupby


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # Bottom-up Dynamic Programming + Prefix Sum:
        # O(w + n * k) time, O(k) space, where w is the
        # size of word

        mod_factor = 10**9 + 7
        char_groups = []
        original_strings = 1
        for _, substring in groupby(word):
            streak = len(list(substring))
            char_groups.append(streak)
            original_strings *= streak
            original_strings %= mod_factor
        n = len(char_groups)
        if k <= n:
            return original_strings
        prev_dp = [0] * (k + 1)
        for chars_remaining in range(1, k + 1):
            prev_dp[chars_remaining] = 1
        dp = [0] * (k + 1)
        for i in reversed(range(n)):
            dp = [0] * (k + 1)
            prefix_sum = [0]
            for chars_remaining in range(k + 1):
                prefix_sum.append(prefix_sum[-1] + prev_dp[chars_remaining])
            for chars_remaining in range(k + 1):
                dp[chars_remaining] += (
                    prefix_sum[chars_remaining]
                    - prefix_sum[max(0, chars_remaining - char_groups[i])]
                )
                dp[chars_remaining] %= mod_factor
            prev_dp = dp
        return (original_strings - dp[k]) % mod_factor
