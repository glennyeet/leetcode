class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # Simulation: O(m * n) time, O(m * n) space

        grid = []
        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == n - 1:
                    row.append(".")
                else:
                    row.append("#")
            row = "".join(row)
            grid.append(row)
        return grid
