class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # Greedy: O(n) time, O(1) space, where n is the
        # size of s

        cur_num = 0
        longest_len = 0
        for digit in reversed(s):
            if digit == "0":
                longest_len += 1
            elif digit == "1" and cur_num + (1 << longest_len) <= k:
                cur_num += 1 << longest_len
                longest_len += 1
        return longest_len
