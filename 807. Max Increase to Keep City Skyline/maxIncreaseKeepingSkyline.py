class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxSum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxX = max(grid[i])
                maxY = 0
                for k in range(len(grid)):
                    if grid[k][j] > maxY:
                        maxY = grid[k][j]
                maxSum += min(maxX, maxY) - grid[i][j]
        return maxSum
