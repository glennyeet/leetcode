from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Math: O(n) time, O(1) space, where n is the size
        # of nums

        return sum(nums) % k
