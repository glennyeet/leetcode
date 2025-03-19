from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Greedy: O(n) time, O(n) space

        n = len(nums)
        result = nums.copy()
        min_operations = 0
        for i in range(n - 2):
            if not result[i]:
                result[i] ^= 1
                result[i + 1] ^= 1
                result[i + 2] ^= 1
                min_operations += 1
        if not result[-1] or not result[-2]:
            return -1
        return min_operations
