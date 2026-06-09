from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Greedy: O(n) time, O(1) space, where n is the size
        # of nums

        return (max(nums) - min(nums)) * k
