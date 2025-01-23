class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Array: O(m * n) time, O(m + n) space

        m = len(grid)
        n = len(grid[0])
        row_counter = [0] * m
        col_counter = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_counter[i] += 1
                    col_counter[j] += 1
        connected_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and max(row_counter[i], col_counter[j]) > 1:
                    connected_servers += 1
        return connected_servers
