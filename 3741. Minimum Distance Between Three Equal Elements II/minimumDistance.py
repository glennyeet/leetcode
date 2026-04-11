from typing import List
from collections import defaultdict


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Hash Table + Sliding Window: O(n) time, O(n) space

        min_dist = float("inf")
        value_to_indices = defaultdict(list)
        for i, num in enumerate(nums):
            value_to_indices[num].append(i)
        for value in value_to_indices:
            indices = value_to_indices[value]
            m = len(indices)
            if m < 3:
                continue
            for l in range(2, m):
                i = indices[l - 2]
                j = indices[l - 1]
                k = indices[l]
                min_dist = min(min_dist, abs(i - j) + abs(j - k) + abs(k - i))
        if min_dist == float("inf"):
            return -1
        return min_dist
