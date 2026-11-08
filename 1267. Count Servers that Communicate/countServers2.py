class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # Matrix: O(m * n) time, O(m + n) space

        m = len(grid)
        n = len(grid[0])
        row_count = [0] * m
        col_count = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_count[i] += 1
                    col_count[j] += 1
        communicable_servers = 0
        for i in range(m):
            for j in range(n):
                communicable_servers += grid[i][j] and (
                    row_count[i] > 1 or col_count[j] > 1
                )
        return communicable_servers
