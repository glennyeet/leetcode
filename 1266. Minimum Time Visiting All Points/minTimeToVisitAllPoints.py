from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Math: O(n) time, O(1) space, where n is the size of points

        min_time = 0
        cur_x, cur_y = points[0]
        for x, y in points:
            min_time += max(abs(x - cur_x), abs(y - cur_y))
            cur_x = x
            cur_y = y
        return min_time
