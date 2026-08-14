class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # Sliding Window: O(n) time, O(1) space, where n is the
        # size of s

        max_length = 0
        l = 0
        char_counter = [0] * 26
        for r, char in enumerate(s):
            char_counter_index = ord(char) - ord("a")
            char_counter[char_counter_index] += 1
            while l <= r and char_counter[char_counter_index] > 2:
                char_counter[ord(s[l]) - ord("a")] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
