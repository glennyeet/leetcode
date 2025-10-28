from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Simulation: O(n^2 * m) time, O(n) space, where m
        # is max(nums)

        n = len(nums)
        nums_sum = sum(nums)
        valid_selections = 0
        for i, num in enumerate(nums):
            if num != 0:
                continue
            nums_copy = nums.copy()
            cur_sum = nums_sum
            j = i
            left = True
            while cur_sum > 0 and 0 <= j < n:
                if nums_copy[j] > 0:
                    nums_copy[j] -= 1
                    cur_sum -= 1
                    left = not left
                if left:
                    j -= 1
                else:
                    j += 1
            if cur_sum == 0:
                valid_selections += 1
            nums_copy = nums.copy()
            cur_sum = nums_sum
            j = i
            left = False
            while cur_sum > 0 and 0 <= j < n:
                if nums_copy[j] > 0:
                    nums_copy[j] -= 1
                    cur_sum -= 1
                    left = not left
                if left:
                    j -= 1
                else:
                    j += 1
            if cur_sum == 0:
                valid_selections += 1
        return valid_selections
