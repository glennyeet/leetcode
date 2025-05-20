from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Sweep Line Algorithm: O(n + q) time, O(n) space, where q is the
        # size of queries

        n = len(nums)
        decrement_delta = [0] * (n + 1)
        for l, r in queries:
            decrement_delta[l] += 1
            decrement_delta[r + 1] -= 1
        possible_decrements = 0
        for i, num in enumerate(nums):
            possible_decrements += decrement_delta[i]
            if possible_decrements < num:
                return False
        return True
