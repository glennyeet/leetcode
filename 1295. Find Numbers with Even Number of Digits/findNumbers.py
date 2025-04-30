from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Brute Force: O(n) time, O(1) space, where
        # n is the size of nums

        even_digits = 0
        for num in nums:
            even_digits += len(str(num)) % 2 == 0
        return even_digits
