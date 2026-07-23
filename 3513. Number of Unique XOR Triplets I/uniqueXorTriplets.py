from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Bit Manipulation: O(log(n)) time, O(1) space,
        # where n is the size of nums

        n = len(nums)
        if n <= 2:
            return n
        count = 0
        while n > 0:
            n //= 2
            count += 1
        return 2**count
