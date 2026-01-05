from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Greedy: O(n ^ 2) time, O(1) space

        n = len(matrix)
        abs_sum = 0
        negative_nums = 0
        min_abs_num = float("inf")
        for i in range(n):
            for j in range(n):
                abs_num = abs(matrix[i][j])
                abs_sum += abs_num
                negative_nums += matrix[i][j] < 0
                min_abs_num = min(min_abs_num, abs_num)
        if negative_nums % 2 == 0:
            return abs_sum
        else:
            return abs_sum - 2 * min_abs_num
