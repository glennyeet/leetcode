from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Math: O((m * n) * log(m * n)) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        nums = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != grid[0][0] % x:
                    return -1
                nums.append(grid[i][j])
        nums.sort()
        middle_num = nums[len(nums) // 2]
        min_operations = 0
        for num in nums:
            min_operations += (abs(num - middle_num)) // x
        return min_operations
