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
            leftmost_position = fruits[l][0]
            rightmost_position = fruits[r][0]
            while (
                l <= r
                and min(
                    startPos - 2 * leftmost_position + rightmost_position,
                    2 * rightmost_position - startPos - leftmost_position,
                )
                > k
            ):
                cur_fruits -= fruits[l][1]
                l += 1
                leftmost_position = fruits[l][0]
            max_fruits = max(max_fruits, cur_fruits)
        return max_fruits
