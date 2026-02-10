from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Hash Table: O(n^2) time, O(n) space

        n = len(nums)
        max_length = 0
        for i in range(n):
            even_nums = set()
            odd_nums = set()
            if nums[i] % 2 == 0:
                even_nums.add(nums[i])
            else:
                odd_nums.add(nums[i])
            for j in range(i + 1, n):
                if nums[j] % 2 == 0:
                    even_nums.add(nums[j])
                else:
                    odd_nums.add(nums[j])
                if len(even_nums) == len(odd_nums):
                    max_length = max(max_length, j - i + 1)
        return max_length
