from typing import List
from functools import cache
from bisect import bisect_left, bisect_right


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Top-down DP + Binary Search: O(n * log(n) + m * log(m) + n * log(m)) time,
        # O(n + m) space, where m is the size of walls

        n = len(robots)
        sorted_walls = sorted(walls)
        ranges = []
        for robot, max_range in zip(robots, distance):
            ranges.append((robot, max_range))
        ranges.sort()

        @cache
        def dp(i: int, left_boundary: int) -> int:
            if i == n:
                return 0
            max_walls_destroyed = 0
            left_boundary = max(left_boundary, ranges[i][0] - ranges[i][1])
            max_walls_destroyed = max(
                max_walls_destroyed,
                dp(i + 1, ranges[i][0] + 1)
                + bisect_right(sorted_walls, ranges[i][0])
                - bisect_left(sorted_walls, left_boundary),
            )
            right_boundary = ranges[i][0] + ranges[i][1]
            if i + 1 < n:
                right_boundary = min(right_boundary, ranges[i + 1][0] - 1)
            max_walls_destroyed = max(
                max_walls_destroyed,
                dp(i + 1, right_boundary + 1)
                + bisect_right(sorted_walls, right_boundary)
                - bisect_left(sorted_walls, ranges[i][0]),
            )
            return max_walls_destroyed

        return dp(0, 0)
