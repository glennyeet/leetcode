from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Brute Force: O(2^n) time, O(2^n) space, where
        # n is numRows

        pascals_triangle = []
        for i in range(numRows):
            if i == 0:
                pascals_triangle.append([1])
            else:
                row = [1]
                for j, num in enumerate(pascals_triangle[-1]):
                    if j + 1 == len(pascals_triangle[-1]):
                        row.append(1)
                    else:
                        row.append(num + pascals_triangle[-1][j + 1])
                pascals_triangle.append(row)
        return pascals_triangle
