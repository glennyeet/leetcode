from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Brute Force: O(1) time, O(1) space

        if (
            nums[1] + nums[2] <= nums[0]
            or nums[0] + nums[2] <= nums[1]
            or nums[0] + nums[1] <= nums[2]
        ):
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return "isosceles"
        else:
            return "scalene"
