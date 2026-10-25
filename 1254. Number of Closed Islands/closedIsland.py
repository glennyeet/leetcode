class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # DFS: O(n * m) time, O(n * m) space

        n = len(grid)
        m = len(grid[0])
        res_grid = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res_grid[i][j] = grid[i][j]

        def dfs(i: int, j: int) -> bool:
            if not (0 <= i < n and 0 <= j < m):
                return False
            if res_grid[i][j]:
                return True
            res_grid[i][j] = 1
            return dfs(i + 1, j) & dfs(i - 1, j) & dfs(i, j + 1) & dfs(i, j - 1)

        return sum(dfs(i, j) for i in range(n) for j in range(m) if not res_grid[i][j])
