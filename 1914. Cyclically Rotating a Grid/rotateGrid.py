from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Simulation: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        rotated_grid = [[0] * n for _ in range(m)]
        layers = min(m, n) // 2
        for layer in range(layers):
            i_start = j_start = layer
            i_end = m - layer - 1
            j_end = n - layer - 1
            height = m - 2 * layer
            width = n - 2 * layer
            perimeter = (height + width - 2) * 2
            layer_nums = []
            for j in range(width - 1):
                layer_nums.append(grid[i_start][j_start + j])
            for i in range(height - 1):
                layer_nums.append(grid[i_start + i][j_end])
            for j in range(width - 1):
                layer_nums.append(grid[i_end][j_end - j])
            for i in range(height - 1):
                layer_nums.append(grid[i_end - i][j_start])
            l = k % perimeter
            for j in range(width - 1):
                rotated_grid[i_start][j_start + j] = layer_nums[l]
                l = (l + 1) % perimeter
            for i in range(height - 1):
                rotated_grid[i_start + i][j_end] = layer_nums[l]
                l = (l + 1) % perimeter
            for j in range(width - 1):
                rotated_grid[i_end][j_end - j] = layer_nums[l]
                l = (l + 1) % perimeter
            for i in range(height - 1):
                rotated_grid[i_end - i][j_start] = layer_nums[l]
                l = (l + 1) % perimeter
        return rotated_grid
