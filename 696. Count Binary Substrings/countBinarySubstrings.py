class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Counting: O(n) time, O(n) space, where n is the size of s

        streaks = []
        cur_streak = 0
        streak_bit = s[0]
        for bit in s:
            if bit == streak_bit:
                cur_streak += 1
            else:
                streaks.append(cur_streak)
                cur_streak = 1
                streak_bit = bit
        else:
            streaks.append(cur_streak)
        valid_substrings = 0
        for i in range(len(streaks) - 1):
            valid_substrings += min(streaks[i], streaks[i + 1])
        return valid_substrings
