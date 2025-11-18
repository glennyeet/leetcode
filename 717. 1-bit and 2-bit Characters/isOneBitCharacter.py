from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Greedy: O(n) time, O(1) space

        n = len(bits)
        i = 0
        is_one_bit = False
        while i < n:
            if bits[i] == 0:
                i += 1
                is_one_bit = True
            else:
                i += 2
                is_one_bit = False
        return i == n and is_one_bit
