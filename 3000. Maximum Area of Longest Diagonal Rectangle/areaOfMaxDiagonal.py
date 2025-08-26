from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # One-pass: O(n) time, O(1) space, where n is the size of
        # dimensions

        longest_diagonal_squared = 0
        max_area = 0
        for length, width in dimensions:
            diagonal_squared = length**2 + width**2
            area = length * width
            if diagonal_squared > longest_diagonal_squared:
                longest_diagonal_squared = diagonal_squared
                max_area = area
            elif diagonal_squared == longest_diagonal_squared:
                max_area = max(max_area, area)
        return max_area
