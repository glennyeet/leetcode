from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Sliding Window: O(s * n) time, O(1) space, where s is r - l

        n = len(nums)
        min_sum = float("inf")
        for size in range(l, r + 1):
            cur_sum = 0
            i = 0
            for j in range(n):
                cur_sum += nums[j]
                if j - i + 1 < size:
                    continue
                if cur_sum > 0:
                    min_sum = min(min_sum, cur_sum)
                cur_sum -= nums[i]
                i += 1
        if min_sum == float("inf"):
            return -1
        return min_sum
