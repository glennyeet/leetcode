class Solution:
    def maxOperations(self, s: str) -> int:
        # Greedy: O(n) time, O(1) space, where
        # n is the size of s

        max_operations = 0
        shifts = 0
        prev_bit = s[-1]
        for bit in reversed(s):
            if bit == "1" and prev_bit == "0":
                shifts += 1
            if bit == "1":
                max_operations += shifts
            prev_bit = bit
        return max_operations
