from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Hash Table + Sliding Window: O(n) time, O(n) space, where n is
        # the size of nums

        nums_counter = Counter()
        longest_good_subarray = 0
        l = 0
        for r, num in enumerate(nums):
            nums_counter[num] += 1
            while l <= r and nums_counter[num] > k:
                nums_counter[nums[l]] -= 1
                l += 1
            longest_good_subarray = max(longest_good_subarray, r - l + 1)
        return longest_good_subarray
