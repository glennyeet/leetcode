from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window: O(n) time, O(n) space, where n is the size
        # of s

        left = 0
        char_counter = Counter()
        max_char_count = 0
        longest_substring = 0
        for right, char in enumerate(s):
            char_counter[char] += 1
            max_char_count = max(max_char_count, char_counter[char])
            while right - left + 1 - max_char_count > k:
                char_counter[s[left]] -= 1
                left += 1
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring
