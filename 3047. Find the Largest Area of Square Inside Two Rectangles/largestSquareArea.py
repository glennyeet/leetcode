from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        # Geometry: O(n^2) time, O(1) space

        n = len(bottomLeft)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])
                if x1 > x2 or y1 > y2:
                    continue
                s1 = x2 - x1
                s2 = y2 - y1
                max_area = max(max_area, min(s1, s2) ** 2)
        return max_area
