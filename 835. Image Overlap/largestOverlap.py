from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # Matrix: O(n^2 * m^2) time, O(1) space

        n = len(img1)
        m = len(img1[0])
        max_overlaps = 0
        for di in range(-n + 1, n):
            for dj in range(-m + 1, m):
                overlaps = 0
                for i in range(n):
                    ni = i + di
                    if 0 <= ni < n:
                        for j in range(m):
                            nj = j + dj
                            if 0 <= nj < m and img1[i][j] + img2[ni][nj] == 2:
                                overlaps += 1
                max_overlaps = max(max_overlaps, overlaps)
        return max_overlaps
