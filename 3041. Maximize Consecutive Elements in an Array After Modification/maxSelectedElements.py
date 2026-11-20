from collections import Counter
from functools import cache
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Hash Table + Bottom-up DP: O(n) time, O(n) space, where n is the size
        # of nums

        nums_counter = Counter(nums)

        @cache
        def dp(cur_num: int, is_original_number: bool) -> int:
            max_selected = 0
            if cur_num in nums_counter:
                max_selected = max(max_selected, 1 + dp(cur_num + 1, True))
            if cur_num - 1 in nums_counter:
                if nums_counter[cur_num - 1] >= 2 or (
                    not is_original_number and nums_counter[cur_num - 1] >= 1
                ):
                    max_selected = max(max_selected, 1 + dp(cur_num + 1, False))
            return max_selected

        max_selected = 0
        for num in nums_counter:
            max_selected = max(max_selected, dp(num, False))
            max_selected = max(max_selected, dp(num + 1, False))
        return max_selected
