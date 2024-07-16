class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                grid[i] = [bit ^ 1 for bit in grid[i]]
        for j in range(len(grid[0])):
            zeroCount = 0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    zeroCount += 1
            if zeroCount > len(grid) // 2:
                for i in range(len(grid)):
                    grid[i][j] ^= 1
        score = 0
        for i in range(len(grid)):
            score += int("".join([str(bit) for bit in grid[i]]), 2)
        return score
