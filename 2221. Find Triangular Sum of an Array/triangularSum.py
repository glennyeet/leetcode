from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Simulation: O(n^2) time, O(n) space, where
        # n is the size of nums

        cur_nums = nums.copy()
        while len(cur_nums) > 1:
            new_nums = []
            for i in range(len(cur_nums) - 1):
                new_nums.append((cur_nums[i] + cur_nums[i + 1]) % 10)
            cur_nums = new_nums
        return cur_nums[0]
