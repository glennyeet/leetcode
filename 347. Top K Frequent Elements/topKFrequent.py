from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash Table + Sorting: O(n * log(n)) time, O(n) space, where
        # n is the size of nums

        nums_counter = Counter(nums)
        sorted_frequencies = sorted(
            nums_counter.items(), key=lambda x: x[1], reverse=True
        )
        most_frequent_nums = []
        for num, _ in sorted_frequencies[:k]:
            most_frequent_nums.append(num)
        return most_frequent_nums
