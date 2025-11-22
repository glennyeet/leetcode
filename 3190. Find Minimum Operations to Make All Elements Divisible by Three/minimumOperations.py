from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Math: O(n) time, O(1) space, where n is the size of nums

        min_operations = 0
        for num in nums:
            min_operations += min(num % 3, (num // 3 + 1) * 3 - num)
        return min_operations
