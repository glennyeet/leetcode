from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Hash Table + Sliding Window: O(n) time, O(n) space,
        # where n is the size of nums

        max_score = 0
        subarray_sum = 0
        subarray_nums = set()
        i = 0
        for j, num in enumerate(nums):
            if num in subarray_nums:
                while i < j:
                    subarray_sum -= nums[i]
                    subarray_nums.remove(nums[i])
                    i += 1
                    if nums[i - 1] == num:
                        break
            subarray_sum += num
            subarray_nums.add(num)
            max_score = max(max_score, subarray_sum)
        return max_score
