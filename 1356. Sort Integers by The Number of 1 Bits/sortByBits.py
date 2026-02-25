from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Bit Manipulation: O(n * log(n)) time, O(n) space,
        # where n is the size of arr

        return sorted(arr, key=lambda x: (x.bit_count(), x))
