from typing import List
from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Hash Table: O(n * log(n)) time, O(n) space

        x_groups = defaultdict(list)
        y_groups = defaultdict(list)
        covered_buildings = set()
        for x, y in buildings:
            x_groups[x].append(y)
            y_groups[y].append(x)
            covered_buildings.add((x, y))
        for x in x_groups:
            x_groups[x].sort()
            covered_buildings.discard((x, x_groups[x][0]))
            covered_buildings.discard((x, x_groups[x][len(x_groups[x]) - 1]))
        for y in y_groups:
            y_groups[y].sort()
            covered_buildings.discard((y_groups[y][0], y))
            covered_buildings.discard((y_groups[y][len(y_groups[y]) - 1], y))
        return len(covered_buildings)
