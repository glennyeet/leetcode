from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Greedy: O(n) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        for i in reversed(range(n - 2)):
            a = sorted_nums[i]
            b = sorted_nums[i + 1]
            c = sorted_nums[i + 2]
            if a + b > c:
                return a + b + c
        return 0
