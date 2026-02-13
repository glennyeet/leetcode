from itertools import combinations


class Solution:
    def longestBalanced(self, s: str) -> int:
        # Hash Table + Prefix Sum: O(n) time, O(n) space, where n is the size of s

        one_distinct_char_max_length = 0
        streak_char = None
        cur_streak = 0
        for char in s:
            if char != streak_char:
                streak_char = char
                cur_streak = 1
            else:
                cur_streak += 1
            one_distinct_char_max_length = max(one_distinct_char_max_length, cur_streak)

        def find_two_distinct_chars_max_length(c1: str, c2: str) -> int:
            cur_delta = 0
            last_seen_delta = {}
            last_seen_delta[cur_delta] = 0
            max_length = 0
            for i, char in enumerate(s):
                if char == c1:
                    cur_delta += 1
                elif char == c2:
                    cur_delta -= 1
                else:
                    cur_delta = 0
                    last_seen_delta = {}
                    last_seen_delta[cur_delta] = i + 1
                    continue
                if cur_delta in last_seen_delta:
                    max_length = max(max_length, i + 1 - last_seen_delta[cur_delta])
                else:
                    last_seen_delta[cur_delta] = i + 1
            return max_length

        two_distinct_chars_max_length = 0
        for c1, c2 in combinations("abc", 2):
            two_distinct_chars_max_length = max(
                two_distinct_chars_max_length,
                find_two_distinct_chars_max_length(c1, c2),
            )
        three_distinct_chars_max_length = 0
        cur_ab_delta = 0
        cur_ac_delta = 0
        last_seen_delta = {}
        last_seen_delta[(cur_ab_delta, cur_ac_delta)] = 0
        for i, char in enumerate(s):
            if char == "a":
                cur_ab_delta += 1
                cur_ac_delta += 1
            elif char == "b":
                cur_ab_delta -= 1
            else:
                cur_ac_delta -= 1
            if (cur_ab_delta, cur_ac_delta) in last_seen_delta:
                three_distinct_chars_max_length = max(
                    three_distinct_chars_max_length,
                    i + 1 - last_seen_delta[(cur_ab_delta, cur_ac_delta)],
                )
            else:
                last_seen_delta[(cur_ab_delta, cur_ac_delta)] = i + 1
        return max(
            one_distinct_char_max_length,
            two_distinct_chars_max_length,
            three_distinct_chars_max_length,
        )
