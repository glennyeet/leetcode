from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Sorting: O(n * log(n)) time, O(n) space,
        # where n is the size of nums

        cost2, cost3, *_ = sorted(nums[1:])
        return nums[0] + cost2 + cost3
