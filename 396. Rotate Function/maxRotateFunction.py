from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Math: O(n) time, O(1) space

        n = len(nums)
        nums_sum = sum(nums)
        F0 = 0
        for i, num in enumerate(nums):
            F0 += i * num
        F_max = F0
        F_prev = F0
        for i in range(1, n):
            F_cur = F_prev - (n - 1) * nums[n - i] + nums_sum - nums[n - i]
            F_max = max(F_max, F_cur)
            F_prev = F_cur
        return F_max
