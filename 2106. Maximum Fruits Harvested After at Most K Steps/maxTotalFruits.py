from typing import List
from bisect import bisect_left


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Binary Search + Sliding Window: O(n) time, O(1) space, where n is the size
        # of fruits

        min_position = bisect_left(fruits, [startPos - k, 0])
        max_position = bisect_left(fruits, [startPos + k + 1, 0])
        max_fruits = 0
        cur_fruits = 0
        l = min_position
        for r in range(min_position, max_position):
            cur_fruits += fruits[r][1]
            left_steps = fruits[l][0]
            right_steps = fruits[r][0]
            while (
                l <= r
                and min(
                    2 * right_steps - startPos - left_steps,
                    startPos - 2 * left_steps + right_steps,
                )
                > k
            ):
                cur_fruits -= fruits[l][1]
                l += 1
                left_steps = fruits[l][0]
            max_fruits = max(max_fruits, cur_fruits)
        return max_fruits
