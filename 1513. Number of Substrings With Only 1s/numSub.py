class Solution:
    def numSub(self, s: str) -> int:
        # Math: O(n) time, O(1) space, where n is the size of s

        mod_factor = 10**9 + 7
        streak = 0
        valid_substrings = 0
        for bit in s:
            if bit == "0":
                streak = 0
            else:
                streak += 1
            valid_substrings = (valid_substrings + streak) % mod_factor
        return valid_substrings
