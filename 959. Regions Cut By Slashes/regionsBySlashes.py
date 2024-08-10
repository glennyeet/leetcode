class Solution:
    def find(self, parent: list[int], x: int) -> int:
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent: list[int], a: int, b: int, size: int) -> int:
        parentA = self.find(parent, a)
        parentB = self.find(parent, b)
        if parentA != parentB:
            parent[parentA] = parentB
            size -= 1
        return size

    def regionsBySlashes(self, grid: List[str]) -> int:
        size = len(grid) * len(grid) * 4
        parent = list(range(size))
        # top = 0, right = 1, bottom = 2, left = 3
        for i in range(len(grid)):
            for j in range(len(grid)):
                cellIndex = i * len(grid) + j
                if i < len(grid) - 1:
                    size = self.union(
                        parent, 4 * cellIndex + 2, (cellIndex + len(grid)) * 4, size
                    )
                if j < len(grid) - 1:
                    size = self.union(
                        parent, 4 * cellIndex + 1, 4 * (cellIndex + 1) + 3, size
                    )
                if grid[i][j] == "/":
                    size = self.union(parent, 4 * cellIndex, 4 * cellIndex + 3, size)
                    size = self.union(
                        parent, 4 * cellIndex + 1, 4 * cellIndex + 2, size
                    )
                elif grid[i][j] == "\\":
                    size = self.union(parent, 4 * cellIndex, 4 * cellIndex + 1, size)
                    size = self.union(
                        parent, 4 * cellIndex + 2, 4 * cellIndex + 3, size
                    )
                else:
                    size = self.union(parent, 4 * cellIndex, 4 * cellIndex + 1, size)
                    size = self.union(
                        parent, 4 * cellIndex + 1, 4 * cellIndex + 2, size
                    )
                    size = self.union(
                        parent, 4 * cellIndex + 2, 4 * cellIndex + 3, size
                    )
        return size
