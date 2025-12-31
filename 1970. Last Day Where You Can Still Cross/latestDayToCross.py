from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # Union Find + Hash Table: O(m * n + c * α(m * n)) time, O(m * n) space,
        # where m is row, n is col, and c is the size of cells

        parent = {}
        for r in range(row):
            for c in range(col):
                parent[(r, c)] = (r, c)
        left = -1
        right = -2
        parent[left] = left
        parent[right] = right
        directions = [
            (1, 0),
            (1, 1),
            (1, -1),
            (0, -1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
        ]
        visited = set()

        def find(x: tuple[int, int] | int) -> tuple[int, int] | int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: tuple[int, int] | int, y: tuple[int, int] | int) -> None:
            x_parent = find(x)
            y_parent = find(y)
            parent[x_parent] = y_parent

        for day, (r1, c1) in enumerate(cells):
            r1 -= 1
            c1 -= 1
            for dx, dy in directions:
                r2 = r1 + dx
                c2 = c1 + dy
                if 0 <= r2 < row:
                    if 0 <= c2 < col:
                        if (r2, c2) in visited:
                            union((r1, c1), (r2, c2))
                    else:
                        if c2 == -1:
                            union((r1, c1), left)
                        elif c2 == col:
                            union((r1, c1), right)
                if find(left) == find(right):
                    return day
                visited.add((r1, c1))
        return day
