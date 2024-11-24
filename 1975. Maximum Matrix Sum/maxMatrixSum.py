from math import inf


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        abs_sum = 0
        neg_nums = 0
        min_abs_num = inf
        for row in range(m):
            for col in range(n):
                cur_num = matrix[row][col]
                abs_sum += abs(cur_num)
                min_abs_num = min(min_abs_num, abs(cur_num))
                if cur_num < 0:
                    neg_nums += 1
        if neg_nums % 2 == 0:
            return abs_sum
        else:
            return abs_sum - min_abs_num * 2
