from typing import List
from collections import Counter


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n is the size of nums

        nums_counter = Counter(nums)
        unique_nums = sorted(nums_counter)
        max_used_num = unique_nums[0] - k
        max_distinct_elements = 0
        for num in unique_nums:
            max_used_num = max(max_used_num, num - k)
            new_distinct_elements = min(nums_counter[num], num + k - max_used_num + 1)
            max_distinct_elements += new_distinct_elements
            max_used_num += new_distinct_elements
        return max_distinct_elements
