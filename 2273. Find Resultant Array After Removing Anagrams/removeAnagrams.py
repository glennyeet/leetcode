from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # Hash Table: O(n * m) time, O(n) space, where n
        # is the size of words and m is the size of the
        # largest word in words

        anagram_counter = Counter()
        non_anagrams = []
        for word in words:
            word_counter = Counter(word)
            if word_counter != anagram_counter:
                anagram_counter = word_counter
                non_anagrams.append(word)
        return non_anagrams
