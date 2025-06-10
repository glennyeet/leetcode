from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        # Hash Table: O(n) time, O(n) space,
        # where n is the size of s

        char_counter = Counter(s)
        a1 = 0
        a2 = float("inf")
        for char in char_counter:
            if char_counter[char] % 2:
                a1 = max(a1, char_counter[char])
            else:
                a2 = min(a2, char_counter[char])
        return a1 - a2
