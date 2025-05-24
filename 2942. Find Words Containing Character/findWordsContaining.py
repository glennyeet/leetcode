from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Brute Force: O(n * m) time, O(n) space, where n is the size
        # of words and m is the size of the longest string in words

        valid_indices = []
        for i, word in enumerate(words):
            if x in word:
                valid_indices.append(i)
        return valid_indices
