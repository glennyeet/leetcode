from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_remainder = sum(nums) % p
        if total_remainder == 0:
            return 0
        remainder_prefix_sums = []
        cur_remainder = 0
        remainder_indices = {0: -1}
        min_subarray_length = len(nums)
        for i, num in enumerate(nums):
            cur_remainder = (cur_remainder + num) % p
            remainder = (cur_remainder - total_remainder) % p
            if remainder in remainder_indices:
                min_subarray_length = min(
                    min_subarray_length, i - remainder_indices[remainder]
                )
            remainder_indices[cur_remainder] = i
            remainder_prefix_sums.append(cur_remainder)
        if min_subarray_length == len(nums):
            return -1
        else:
            return min_subarray_length
