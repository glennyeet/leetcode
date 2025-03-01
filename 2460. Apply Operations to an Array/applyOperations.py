from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Brute force: O(n) time, O(n) space

        n = len(nums)
        nums_copy = nums.copy()
        for i in range(n - 1):
            if nums_copy[i] == nums_copy[i + 1]:
                nums_copy[i] *= 2
                nums_copy[i + 1] = 0
        non_zero_nums = []
        zeros_count = 0
        for num in nums_copy:
            if num:
                non_zero_nums.append(num)
            else:
                zeros_count += 1
        return non_zero_nums + [0] * zeros_count
