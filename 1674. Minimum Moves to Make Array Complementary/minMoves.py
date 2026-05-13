from typing import List
from collections import defaultdict


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # Line Sweep: O(n) time, O(n) space

        n = min_moves = len(nums)
        delta = defaultdict(int)
        max_pair_sum = 2
        for i in range(n // 2):
            max_sum = max(nums[i] + limit, nums[n - i - 1] + limit)
            min_sum = min(nums[i] + 1, nums[n - i - 1] + 1)
            pair_sum = nums[i] + nums[n - i - 1]
            max_pair_sum = max(max_pair_sum, pair_sum)
            delta[pair_sum] -= 1
            delta[pair_sum + 1] += 1
            delta[min_sum] -= 1
            delta[max_sum + 1] += 1
        moves = n
        for pair_sum in range(2, max_pair_sum + 1):
            moves += delta[pair_sum]
            min_moves = min(min_moves, moves)
        return min_moves
