from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # Greedy: O(nlog(n)) time, O(n) space, where n is the
        # size of nums

        sorted_nums = sorted(nums)
        min_subsequences = 1
        min_num = sorted_nums[0]
        for num in sorted_nums:
            if num - min_num > k:
                min_num = num
                min_subsequences += 1
        return min_subsequences
