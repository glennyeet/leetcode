from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Prefix sum: O(m * nlog(m * n)) time, O(m * n) space, where
        # m * n are the number of rows and columns in grid

        total = 0
        nums = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] % x != grid[0][0] % x:
                    return -1
                total += grid[row][col]
                nums.append(grid[row][col])
        nums.sort()
        n = len(nums)
        prefix_sum = 0
        min_operations = float("inf")
        for i, num in enumerate(nums):
            left_sum = num * i - prefix_sum
            right_sum = total - prefix_sum - num * (n - i)
            min_operations = min(min_operations, (left_sum + right_sum) // x)
            prefix_sum += num
        return min_operations
