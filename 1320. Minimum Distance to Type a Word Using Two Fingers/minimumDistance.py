from functools import cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        # Top-down DP: O(n) time, O(n) space

        n = len(word)

        def distance(x: int, y: int) -> int:
            if x == 26:
                return 0
            return abs(x // 6 - y // 6) + abs(x % 6 - y % 6)

        @cache
        def dp(word_index: int, other_finger_index: int) -> int:
            if word_index == n:
                return 0
            if word_index == 0:
                cur_finger_index = other_finger_index
            else:
                cur_finger_index = ord(word[word_index - 1]) - ord("A")
            char = ord(word[word_index]) - ord("A")
            return min(
                dp(word_index + 1, other_finger_index)
                + distance(cur_finger_index, char),
                dp(word_index + 1, cur_finger_index)
                + distance(other_finger_index, char),
            )

        return dp(0, 26)
