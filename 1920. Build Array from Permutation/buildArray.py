from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Brute Force: O(n) time, O(n) space

        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans
