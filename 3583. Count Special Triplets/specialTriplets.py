from typing import List
from collections import Counter


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space

        mod_factor = 10**9 + 7
        left_counter = Counter()
        right_counter = Counter(nums)
        special_triplets = 0
        for num in nums:
            right_counter[num] -= 1
            special_triplets = (
                special_triplets + left_counter[num * 2] * right_counter[num * 2]
            ) % mod_factor
            left_counter[num] += 1
        return special_triplets
