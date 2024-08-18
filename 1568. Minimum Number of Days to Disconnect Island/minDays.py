class Solution:
    # Brute force
    # directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # up, right, down, left

    # def dfs(self, grid: list[list[int]], visited: list[list[int]], row: int, col: int):
    #     visited[row][col] = 1
    #     m = len(grid)
    #     n = len(grid[0])
    #     for x, y in self.directions:
    #         newRow = row + x
    #         newCol = col + y
    #         if (
    #             0 <= newRow < m
    #             and 0 <= newCol < n
    #             and grid[newRow][newCol] == 1
    #             and visited[newRow][newCol] == 0
    #         ):
    #             self.dfs(grid, visited, newRow, newCol)

    # def getNumIslands(self, grid: list[list[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     visited = [[0] * n for _ in range(m)]
    #     islands = 0
    #     for row in range(m):
    #         for col in range(n):
    #             if grid[row][col] == 1 and visited[row][col] == 0:
    #                 self.dfs(grid, visited, row, col)
    #                 islands += 1
    #     return islands

    # def minDays(self, grid: List[List[int]]) -> int:
    #     islands = self.getNumIslands(grid)
    #     if islands != 1:
    #         return 0
    #     m = len(grid)
    #     n = len(grid[0])
    #     gridCopy = grid
    #     for row in range(m):
    #         for col in range(n):
    #             if gridCopy[row][col] == 1:
    #                 gridCopy[row][col] = 0
    #                 islands = self.getNumIslands(gridCopy)
    #                 if islands != 1:
    #                     return 1
    #                 gridCopy[row][col] = 1
    #     return 2

    # Tarjan's algorithm
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # up, right, down, left

    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ids = [[-1] * n for _ in range(m)]
        low_link = [[-1] * n for _ in range(m)]
        visited = [[0] * n for _ in range(m)]
        parents = [[(-1, -1)] * n for _ in range(m)]
        lands = 0
        islands = 0
        curr_id = 0
        bridges = 0

        def dfs(row: int, col: int):
            visited[row][col] = 1
            children = 0
            nonlocal lands
            lands += 1
            nonlocal curr_id
            ids[row][col] = curr_id
            low_link[row][col] = curr_id
            curr_id += 1

            for x, y in self.directions:
                newRow = row + x
                newCol = col + y
                if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                    if visited[newRow][newCol] == 0:
                        parents[newRow][newCol] = (row, col)
                        children += 1
                        dfs(newRow, newCol)
                        low_link[row][col] = min(
                            low_link[row][col], low_link[newRow][newCol]
                        )
                        if (
                            parents[row][col] == (-1, -1)
                            and children > 1
                            or parents[row][col] != (-1, -1)
                            and ids[row][col] <= low_link[newRow][newCol]
                        ):
                            nonlocal bridges
                            bridges += 1
                    else:
                        low_link[row][col] = min(
                            low_link[row][col], ids[newRow][newCol]
                        )

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and visited[row][col] == 0:
                    dfs(row, col)
                    islands += 1
        if islands != 1 or lands == 0:
            return 0
        elif bridges != 0 or lands == 1:
            return 1
        else:
            return 2
