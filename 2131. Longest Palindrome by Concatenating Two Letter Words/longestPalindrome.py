from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Hash Table: O(n) time, O(n) space, where n is the
        # size of words

        words_counter = Counter(words)
        longest_palindrome = 0
        palindrome_odd_occurence = False
        for word in words_counter:
            reversed_word = word[::-1]
            if word == reversed_word:
                if words_counter[word] % 2:
                    palindrome_odd_occurence = True
                longest_palindrome += words_counter[word] // 2 * 2 * 2
            else:
                longest_palindrome += (
                    min(words_counter[word], words_counter[reversed_word]) * 2
                )
        return longest_palindrome + int(palindrome_odd_occurence) * 2
