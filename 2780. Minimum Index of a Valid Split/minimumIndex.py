from typing import List
from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Hash map: O(n) time, O(n) space

        n = len(nums)
        counter = Counter(nums)
        dominant_element = max(counter, key=counter.get)
        total_dominant_count = counter[dominant_element]
        left_dominant_count = 0
        for i, num in enumerate(nums):
            if num == dominant_element:
                left_dominant_count += 1
            right_dominant_count = total_dominant_count - left_dominant_count
            if left_dominant_count * 2 > i + 1 and right_dominant_count * 2 > n - i - 1:
                return i
        return -1
