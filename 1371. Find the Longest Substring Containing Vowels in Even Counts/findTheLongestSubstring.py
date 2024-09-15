class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        first_occurrences = {}
        odd_occurrences = 0
        first_occurrences[odd_occurrences] = 0
        max_length = 0
        for i, c in enumerate(s):
            if c in vowels:
                odd_occurrences ^= 1 << vowels.find(c)
            if odd_occurrences not in first_occurrences:
                first_occurrences[odd_occurrences] = i + 1
            else:
                max_length = max(max_length, i + 1 - first_occurrences[odd_occurrences])
        return max_length
