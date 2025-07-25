from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where
        # n is the size of nums

        max_num = float("-inf")
        positive_nums = set()
        for num in nums:
            max_num = max(max_num, num)
            if num > 0:
                positive_nums.add(num)
        if max_num <= 0:
            return max_num
        return sum(positive_nums)
