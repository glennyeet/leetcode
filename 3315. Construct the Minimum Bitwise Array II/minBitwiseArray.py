from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # Bit Manipulation: O(n * log(m)) time, O(n) space,
        # where m is max(nums)

        n = len(nums)
        ans = [-1] * n
        for i, num in enumerate(nums):
            a = -1
            position = 1
            while num & position != 0:
                a = num - position
                position <<= 1
            ans[i] = a
        return ans
