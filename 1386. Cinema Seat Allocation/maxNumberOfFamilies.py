from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Hash Table + Bit Manipulation: O(n) time, O(n) space

        bitmasks = defaultdict(int)
        for row, col in reservedSeats:
            bitmasks[row] |= 1 << col - 1
        max_groups = 2 * n
        two_group_row = 0b1000000001
        one_group_row1 = 0b1000011111
        one_group_row2 = 0b1111100001
        one_group_row3 = 0b1110000111
        for row, mask in bitmasks.items():
            if mask | two_group_row == two_group_row:
                continue
            elif (
                mask | one_group_row1 == one_group_row1
                or mask | one_group_row2 == one_group_row2
                or mask | one_group_row3 == one_group_row3
            ):
                max_groups -= 1
            else:
                max_groups -= 2
        return max_groups
