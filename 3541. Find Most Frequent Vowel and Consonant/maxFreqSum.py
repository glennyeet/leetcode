from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Hash Table: O(n) time, O(1) space, where n is the size of s

        char_counter = Counter(s)
        vowels = ["a", "e", "i", "o", "u"]
        max_vowel = 0
        max_consonant = 0
        for char in char_counter:
            if char in vowels:
                max_vowel = max(max_vowel, char_counter[char])
            else:
                max_consonant = max(max_consonant, char_counter[char])
        return max_vowel + max_consonant
