from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Brute Force: O(n^2) time, O(1) space

        n = len(colors)
        max_dist = 0
        for i in range(n):
            for j in range(n):
                if colors[i] != colors[j]:
                    max_dist = max(max_dist, abs(i - j))
        return max_dist
