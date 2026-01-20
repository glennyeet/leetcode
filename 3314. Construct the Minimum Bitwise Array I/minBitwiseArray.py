from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # Enumeration: O(n * m) time, O(n) space, where m is
        # max(nums)

        n = len(nums)
        ans = [-1] * n
        for i, num in enumerate(nums):
            for a in range(1, num):
                if a | a + 1 == num:
                    ans[i] = a
                    break
        return ans
