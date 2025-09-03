from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Enumeration: O(n^2) time, O(n) space

        n = len(points)
        sorted_points = sorted(points, key=lambda p: (p[0], -p[1]))
        valid_pairs = 0
        for i in range(n):
            _, y1 = sorted_points[i]
            min_y = float("-inf")
            for j in range(i + 1, n):
                _, y2 = sorted_points[j]
                if min_y <= y2 <= y1:
                    valid_pairs += 1
                    min_y = y2 + 1
        return valid_pairs
