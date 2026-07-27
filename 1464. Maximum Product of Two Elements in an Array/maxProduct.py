from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Math: O(n) time, O(1) space

        max_num = -1
        second_max_num = -1
        for num in nums:
            if num > max_num:
                second_max_num = max_num
                max_num = num
            elif num > second_max_num:
                second_max_num = num
        return (max_num - 1) * (second_max_num - 1)
