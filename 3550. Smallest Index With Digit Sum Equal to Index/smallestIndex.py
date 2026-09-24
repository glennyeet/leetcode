from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # Math: O(n * log(m)) time, O(1) space,
        # where n is the size of nums and m is the
        # number of digits of max(nums)

        def find_digit_sum(num: int) -> int:
            cur_num = num
            digit_sum = 0
            while cur_num:
                digit_sum += cur_num % 10
                cur_num //= 10
            return digit_sum

        for i, num in enumerate(nums):
            if find_digit_sum(num) == i:
                return i
        return -1
