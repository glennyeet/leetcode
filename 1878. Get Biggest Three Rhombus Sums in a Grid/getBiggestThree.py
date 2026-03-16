from typing import List
from sortedcontainers import SortedSet


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Enumeration: O(m * n * (m * n)^2) time O(m * n * (m * n)^2) space

        m = len(grid)
        n = len(grid[0])

        def get_rhombus_sum(centre_x: int, centre_y: int, length: int) -> int:
            if length == 0:
                return grid[centre_x][centre_y]
            cur_x = centre_x - length
            cur_y = centre_y
            rhombus_sum = 0
            directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
            for dx, dy in directions:
                for _ in range(length):
                    cur_x += dx
                    cur_y += dy
                    rhombus_sum += grid[cur_x][cur_y]
            return rhombus_sum

        max_rhombus_sums = SortedSet()
        for centre_x in range(m):
            for centre_y in range(n):
                length = 0
                while (
                    centre_x - length >= 0
                    and centre_x + length < m
                    and centre_y - length >= 0
                    and centre_y + length < n
                ):
                    rhombus_sum = get_rhombus_sum(centre_x, centre_y, length)
                    max_rhombus_sums.add(rhombus_sum)
                    if len(max_rhombus_sums) > 3:
                        max_rhombus_sums.remove(max_rhombus_sums[0])
                    length += 1
        return list(reversed(max_rhombus_sums))
