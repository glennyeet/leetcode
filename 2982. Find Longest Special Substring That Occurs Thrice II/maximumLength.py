from collections import defaultdict, Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        char_counter = defaultdict(Counter)
        current_char = None
        streak = 0

        def store_streaks():
            for streak_len in range(1, streak + 1):
                char_counter[current_char][streak_len] += streak + 1 - streak_len

        for char in s:
            if char != current_char:
                store_streaks()
                current_char = char
                streak = 1
            else:
                streak += 1
        else:
            store_streaks()
        max_len = -1
        for char in char_counter:
            for streak_len in char_counter[char]:
                if char_counter[char][streak_len] >= 3:
                    max_len = max(max_len, streak_len)
        return max_len
