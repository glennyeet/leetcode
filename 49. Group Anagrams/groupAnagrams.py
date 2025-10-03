from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash Table: O(m * n) time, O(m * n) space, where m
        # is the size of strs, and n is the size of the longest
        # string in strs

        groups = defaultdict(list)
        for word in strs:
            letter_counter = [0] * 26
            for letter in word:
                letter_counter[ord(letter) - ord("a")] += 1
            groups[tuple(letter_counter)].append(word)
        return list(groups.values())
