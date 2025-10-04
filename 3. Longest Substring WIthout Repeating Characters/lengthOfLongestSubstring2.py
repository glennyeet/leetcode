from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash Table + Sliding Window: O(n) time, O(n) space

        n = len(s)
        if n == 0:
            return 0
        left = 0
        longest_substring = 0
        char_counter = Counter()
        for right, char in enumerate(s):
            char_counter[char] += 1
            if char_counter[char] > 1:
                longest_substring = max(longest_substring, right - left)
                while left < right and char_counter[char] > 1:
                    char_counter[s[left]] -= 1
                    left += 1
        else:
            longest_substring = max(longest_substring, n - left)
        return longest_substring
