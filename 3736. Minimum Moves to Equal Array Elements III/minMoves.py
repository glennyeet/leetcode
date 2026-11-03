from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Math: O(n) time, O(1) space, where n
        # is the size of nums

        max_num = max(nums)
        min_moves = 0
        for num in nums:
            min_moves += max_num - num
        return min_moves
