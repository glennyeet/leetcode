from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Hash Table: O(n * log(m)) time, O(n) space, where m
        # is the number of bits of max(nums)

        n = len(nums)

        def reverse(num: int) -> int:
            return int(str(num)[::-1])

        reversed_num_indices = {}
        min_abs_dist = float("inf")
        for j in range(n):
            if nums[j] in reversed_num_indices:
                i = reversed_num_indices[nums[j]]
                min_abs_dist = min(min_abs_dist, abs(i - j))
            reversed_num_indices[reverse(nums[j])] = j
        if min_abs_dist == float("inf"):
            return -1
        return min_abs_dist
