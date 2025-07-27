from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Two Pointers: O(n) time, O(1) space

        n = len(nums)
        left_neq_neighbour = nums[0]
        hills_and_valleys = 0
        for i in range(1, n - 1):
            if nums[i - 1] != nums[i]:
                left_neq_neighbour = nums[i - 1]
            hills_and_valleys += (
                left_neq_neighbour < nums[i]
                and nums[i + 1] < nums[i]
                or left_neq_neighbour > nums[i]
                and nums[i + 1] > nums[i]
            )
        return hills_and_valleys
