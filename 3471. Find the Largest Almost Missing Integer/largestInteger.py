from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Hash Table: O(n) time, O(n) space

        n = len(nums)
        if k == 1:
            largest_almost_missing_num = -1
            nums_counter = Counter(nums)
            for num in nums_counter:
                if nums_counter[num] == 1:
                    largest_almost_missing_num = max(largest_almost_missing_num, num)
            return largest_almost_missing_num
        elif k == n:
            return max(nums)
        first_num_count = nums.count(nums[0])
        last_num_count = nums.count(nums[n - 1])
        if first_num_count == 1 and last_num_count == 1:
            return max(nums[0], nums[n - 1])
        elif first_num_count == 1:
            return nums[0]
        elif last_num_count == 1:
            return nums[n - 1]
        return -1
