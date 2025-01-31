from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # BFS: O(m * n) time, O(m * n) space

        m = len(grid)
        n = len(grid[0])
        labelled_grid = grid.copy()
        island_label = 2
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        island_areas = {}

        def get_island_area(start_node: tuple[int, int]) -> int:
            visited[start_node[0]][start_node[1]] = True
            labelled_grid[start_node[0]][start_node[1]] = island_label
            queue = deque([start_node])
            area = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    x2 = x + dx
                    y2 = y + dy
                    if (
                        0 <= x2 < m
                        and 0 <= y2 < n
                        and not visited[x2][y2]
                        and labelled_grid[x2][y2]
                    ):
                        visited[x2][y2] = True
                        area += 1
                        labelled_grid[x2][y2] = island_label
                        queue.append((x2, y2))
            return area

        for x in range(m):
            for y in range(n):
                if labelled_grid[x][y] and not visited[x][y]:
                    island_areas[island_label] = get_island_area((x, y))
                    island_label += 1

        def get_hypothetical_area(water_block: tuple[int, int]) -> int:
            visited_labels = set()
            area = 1
            for dx, dy in directions:
                x2 = water_block[0] + dx
                y2 = water_block[1] + dy
                if (
                    0 <= x2 < m
                    and 0 <= y2 < n
                    and labelled_grid[x2][y2]
                    and labelled_grid[x2][y2] not in visited_labels
                ):
                    visited_labels.add(labelled_grid[x2][y2])
                    area += island_areas[labelled_grid[x2][y2]]
            return area

        if island_label == 2:
            largest_island = 0
        else:
            largest_island = island_areas[2]
        for x in range(m):
            for y in range(n):
                if not labelled_grid[x][y]:
                    largest_island = max(largest_island, get_hypothetical_area((x, y)))
        return largest_island
