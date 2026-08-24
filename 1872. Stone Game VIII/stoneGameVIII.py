from functools import cache
from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Prefix Sum + Top-down DP + Minimax: O(n) time,
        # O(n) space

        n = len(stones)
        prefix_value = [0]
        for value in stones:
            prefix_value.append(prefix_value[-1] + value)

        @cache
        def dp(i: int) -> int:
            if i == n:
                return 0
            max_delta = float("-inf")
            score = stones[i] + dp(i + 1)
            max_delta = max(max_delta, score)
            score = -(prefix_value[i + 1] + dp(i + 1))
            max_delta = max(max_delta, score)
            return max_delta

        return stones[0] + stones[1] + dp(2)
