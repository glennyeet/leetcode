from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        # Hash map: O(n) time, O(1) space,
        # where n is the length of s

        char_counter = Counter(s)
        min_len = len(s)
        for char in char_counter:
            if char_counter[char] % 2:
                min_len -= char_counter[char] - 1
            else:
                min_len -= char_counter[char] - 2
        return min_len
