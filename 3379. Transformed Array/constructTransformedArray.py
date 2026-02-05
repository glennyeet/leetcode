from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # Simulation: O(n) time, O(n) space

        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            result.append(nums[(i + num) % n])
        return result
