class Solution:
    def possibleStringCount(self, word: str) -> int:
        # One-Pass: O(n) time, O(1) space

        n = len(word)
        original_strings = 1
        char_streak = 1
        streak_char = None
        for i, char in enumerate(word):
            if char != streak_char:
                original_strings += char_streak - 1
                char_streak = 1
                streak_char = char
            else:
                char_streak += 1
            if i == n - 1:
                original_strings += char_streak - 1
        return original_strings
