from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # String: O(n * p * w) time, O(1) space, where n is the
        # size of patterns, p is the size of the string in
        # patterns with max size, and w is the size of word

        substrings = 0
        for pattern in patterns:
            substrings += pattern in word
        return substrings
