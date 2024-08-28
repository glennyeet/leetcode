import collections


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        m = len(grid2)
        n = len(grid2[0])
        visited = [[False] * n for _ in range(m)]
        islands = 0

        def is_sub_island(row, col) -> bool:
            sub_island = True
            land = collections.deque()
            land.append((row, col))
            while len(land) != 0:
                x, y = land.pop()
                visited[x][y] = True
                if grid1[x][y] == 0:
                    sub_island = False
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and grid2[nx][ny] == 1
                        and visited[nx][ny] == False
                    ):
                        visited[nx][ny] = True
                        land.append((nx, ny))
            return sub_island

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and visited[i][j] == False:
                    if is_sub_island(i, j):
                        islands += 1
        return islands
