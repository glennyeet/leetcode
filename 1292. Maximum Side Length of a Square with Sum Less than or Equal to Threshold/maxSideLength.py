from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # 2D Prefix Sum + Binary Search: O(m * n * log(min(m, n))) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = (
                    prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                    + mat[i - 1][j - 1]
                )

        def is_valid_square(i_start: int, i_end: int, j_start: int, j_end: int) -> bool:
            square_sum = (
                prefix_sum[i_end][j_end]
                - prefix_sum[i_start - 1][j_end]
                - prefix_sum[i_end][j_start - 1]
                + prefix_sum[i_start - 1][j_start - 1]
            )
            return square_sum <= threshold

        left = 1
        right = min(m, n)
        max_length = 0
        while left <= right:
            mid = (left + right) // 2
            found_valid_square = False
            for i in range(1, m - mid + 2):
                for j in range(1, n - mid + 2):
                    if is_valid_square(i, i + mid - 1, j, j + mid - 1):
                        found_valid_square = True
                        break
                if found_valid_square:
                    break
            if found_valid_square:
                max_length = mid
                left = mid + 1
            else:
                right = mid - 1
        return max_length
