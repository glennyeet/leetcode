from typing import List
from math import sqrt


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Math: O(n^3) time, O(1) space

        n = len(points)
        max_area = float("-inf")
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    a = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    b = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
                    c = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
                    s = 1 / 2 * (a + b + c)
                    A = sqrt(s * max(s - a, 0) * max(s - b, 0) * max(s - c, 0))
                    max_area = max(max_area, A)
        return max_area
