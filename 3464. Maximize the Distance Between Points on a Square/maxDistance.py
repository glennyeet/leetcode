from typing import List
from bisect import bisect_left


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # Binary Search: O(log(s) * n * k * log(n)) time, O(n) space, where s
        # is side

        n = len(points)
        l = 1
        r = side
        top_points = []
        right_points = []
        bottom_points = []
        left_points = []
        for x, y in points:
            if y == 0:
                bottom_points.append((x, y))
            elif y == side:
                top_points.append((x, y))
            elif x == 0:
                if y != 0 and y != side:
                    left_points.append((x, y))
            else:
                if y != 0 and y != side:
                    right_points.append((x, y))
        unwrapped_points = []
        for x, y in bottom_points:
            unwrapped_points.append(x)
        for x, y in right_points:
            unwrapped_points.append(side + y)
        for x, y in top_points:
            unwrapped_points.append(side * 2 + (side - x))
        for x, y in left_points:
            unwrapped_points.append(side * 3 + (side - y))
        unwrapped_points.sort()

        def is_valid_manhattan_dist(target: int) -> bool:
            for start in range(n):
                cur = start
                selected = 1
                while selected < k:
                    index = bisect_left(
                        unwrapped_points, unwrapped_points[cur] + target
                    )
                    if (
                        index >= len(unwrapped_points)
                        or unwrapped_points[start] + side * 4 - unwrapped_points[index]
                        < target
                    ):
                        break
                    cur = index
                    selected += 1
                if selected == k:
                    return True
            return False

        while l < r:
            m = (l + r + 1) // 2
            if is_valid_manhattan_dist(m):
                l = m
            else:
                r = m - 1
        return l
