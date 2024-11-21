class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        guarded = [[0] * n for _ in range(m)]
        for x, y in guards:
            guarded[x][y] = 2
        for x, y in walls:
            guarded[x][y] = 2
        for gx, gy in guards:
            x = gx - 1
            y = gy
            while x >= 0 and guarded[x][y] != 2:
                if guarded[x][y] == 0:
                    guarded[x][y] = 1
                x -= 1
            x = gx + 1
            while x < m and guarded[x][y] != 2:
                if guarded[x][y] == 0:
                    guarded[x][y] = 1
                x += 1
            x = gx
            y = gy - 1
            while y >= 0 and guarded[x][y] != 2:
                if guarded[x][y] == 0:
                    guarded[x][y] = 1
                y -= 1
            y = gy + 1
            while y < n and guarded[x][y] != 2:
                if guarded[x][y] == 0:
                    guarded[x][y] = 1
                y += 1
        unguarded_cells = 0
        for x in range(m):
            for y in range(n):
                if guarded[x][y] == 0:
                    unguarded_cells += 1
        return unguarded_cells
