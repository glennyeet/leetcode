from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Array: O(n * log(n)) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        for i, num in enumerate(sorted_nums):
            if i != n - 1 and num != i + 1:
                return False
            elif i == n - 1 and num != i:
                return False
        return True
