from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # Simulation: O(n^2) time, O(n) space, where n is
        # the size of nums

        def is_non_decreasing(array: list[int]) -> bool:
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    return False
            return True

        min_operations = 0
        old_nums = nums.copy()
        while not is_non_decreasing(old_nums):
            min_operations += 1
            min_sum = float("inf")
            min_pair_first_index = None
            o = len(old_nums)
            for i in range(o - 1):
                pair_sum = old_nums[i] + old_nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_pair_first_index = i
            new_nums = []
            i = 0
            while i < o:
                if i == min_pair_first_index:
                    new_nums.append(min_sum)
                    i += 2
                else:
                    new_nums.append(old_nums[i])
                    i += 1
            old_nums = new_nums
        return min_operations
