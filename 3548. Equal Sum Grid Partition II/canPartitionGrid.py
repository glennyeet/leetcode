from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Prefix Sum + Hash Table: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        row_prefix_sums = [0] * m
        cur_sum = 0
        for i in range(m):
            for j in range(n):
                cur_sum += grid[i][j]
            row_prefix_sums[i] = cur_sum
        for i in range(m - 1):
            if row_prefix_sums[i] == cur_sum - row_prefix_sums[i]:
                return True
        seen_nums = set()
        if n == 1:
            for i in range(1, m - 1):
                top_section_sum = row_prefix_sums[i]
                bottom_section_sum = cur_sum - row_prefix_sums[i]
                diff = top_section_sum - bottom_section_sum
                if (
                    diff == grid[0][0] or diff == grid[i][0]
                ) and top_section_sum - diff == bottom_section_sum:
                    return True
        else:
            for i in range(m - 1):
                for j in range(n):
                    seen_nums.add(grid[i][j])
                top_section_sum = row_prefix_sums[i]
                bottom_section_sum = cur_sum - row_prefix_sums[i]
                diff = top_section_sum - bottom_section_sum
                if i == 0:
                    if (
                        diff == grid[i][0] or diff == grid[i][n - 1]
                    ) and top_section_sum - diff == bottom_section_sum:
                        return True
                else:
                    if (
                        diff in seen_nums
                        and top_section_sum - diff == bottom_section_sum
                    ):
                        return True
        seen_nums = set()
        if n == 1:
            for i in reversed(range(1, m - 2)):
                top_section_sum = row_prefix_sums[i]
                bottom_section_sum = cur_sum - row_prefix_sums[i]
                diff = bottom_section_sum - top_section_sum
                if (
                    diff == grid[i][0] or diff == grid[m - 1][0]
                ) and bottom_section_sum - diff == top_section_sum:
                    return True
        else:
            for i in reversed(range(1, m)):
                for j in range(n):
                    seen_nums.add(grid[i][j])
                top_section_sum = row_prefix_sums[i - 1]
                bottom_section_sum = cur_sum - row_prefix_sums[i - 1]
                diff = bottom_section_sum - top_section_sum
                if i == m - 1:
                    if (
                        diff == grid[i][0] or diff == grid[i][n - 1]
                    ) and bottom_section_sum - diff == top_section_sum:
                        return True
                else:
                    if (
                        diff in seen_nums
                        and bottom_section_sum - diff == top_section_sum
                    ):
                        return True
        col_prefix_sums = [0] * n
        cur_sum = 0
        for j in range(n):
            for i in range(m):
                cur_sum += grid[i][j]
            col_prefix_sums[j] = cur_sum
        for i in range(n - 1):
            if col_prefix_sums[i] == cur_sum - col_prefix_sums[i]:
                return True
        seen_nums = set()
        if m == 1:
            for j in range(1, n - 1):
                left_section_sum = col_prefix_sums[j]
                right_section_sum = cur_sum - col_prefix_sums[j]
                diff = left_section_sum - right_section_sum
                if (
                    diff == grid[0][0] or diff == grid[0][j]
                ) and left_section_sum - diff == right_section_sum:
                    return True
        else:
            for j in range(n - 1):
                for i in range(m):
                    seen_nums.add(grid[i][j])
                left_section_sum = col_prefix_sums[j]
                right_section_sum = cur_sum - col_prefix_sums[j]
                diff = left_section_sum - right_section_sum
                if j == 0:
                    if (
                        diff == grid[0][j] or diff == grid[m - 1][j]
                    ) and left_section_sum - diff == right_section_sum:
                        return True
                else:
                    if (
                        diff in seen_nums
                        and left_section_sum - diff == right_section_sum
                    ):
                        return True
        seen_nums = set()
        if m == 1:
            for j in reversed(range(1, n - 2)):
                left_section_sum = col_prefix_sums[j]
                right_section_sum = cur_sum - col_prefix_sums[j]
                diff = right_section_sum - left_section_sum
                if (
                    diff == grid[0][j] or diff == grid[0][n - 1]
                ) and right_section_sum - diff == left_section_sum:
                    return True
        else:
            for j in reversed(range(1, n)):
                for i in range(m):
                    seen_nums.add(grid[i][j])
                left_section_sum = col_prefix_sums[j - 1]
                right_section_sum = cur_sum - col_prefix_sums[j - 1]
                diff = right_section_sum - left_section_sum
                if j == n - 1:
                    if (
                        diff == grid[0][j] or diff == grid[m - 1][j]
                    ) and right_section_sum - diff == left_section_sum:
                        return True
                else:
                    if (
                        diff in seen_nums
                        and right_section_sum - diff == left_section_sum
                    ):
                        return True
        return False
