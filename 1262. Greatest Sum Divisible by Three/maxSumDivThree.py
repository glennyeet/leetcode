from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Bottom-up DP: O(n) time, O(1) space, where n is the
        # size of nums

        cur_sum = 0
        min_mod_one = float("inf")
        min_mod_two = float("inf")
        for num in nums:
            cur_sum += num
            if num % 3 == 1:
                min_mod_two = min(min_mod_two, min_mod_one + num)
                min_mod_one = min(min_mod_one, num)
            elif num % 3 == 2:
                min_mod_one = min(min_mod_one, min_mod_two + num)
                min_mod_two = min(min_mod_two, num)
        if cur_sum % 3 == 0:
            return cur_sum
        elif cur_sum % 3 == 1:
            return cur_sum - min_mod_one
        else:
            return cur_sum - min_mod_two
