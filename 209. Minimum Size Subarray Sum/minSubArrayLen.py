from math import inf, isinf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = inf
        subarray_sum = 0
        l = 0
        for r, num in enumerate(nums):
            subarray_sum += num
            while subarray_sum >= target and l <= r:
                min_len = min(min_len, r - l + 1)
                subarray_sum -= nums[l]
                l += 1
        if isinf(min_len):
            return 0
        return min_len
