class Solution:
    def minOperations(self, s: str) -> int:
        # Bit Manipulation: O(n) time, O(1) space

        n = len(s)
        zero_start_mismatches = 0
        one_start_mismatches = 0
        for i in range(n):
            if i % 2 == 0:
                if s[i] == "0":
                    one_start_mismatches += 1
                else:
                    zero_start_mismatches += 1
            else:
                if s[i] == "0":
                    zero_start_mismatches += 1
                else:
                    one_start_mismatches += 1
        return min(zero_start_mismatches, one_start_mismatches)
