from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # Hash Table + BFS + Bit Manipulation: O(m * n * e * 2^(m * n)) time,
        # O(m * n * e * 2^(m * n)) space, where e is energy

        m = len(classroom)
        n = len(classroom[0])
        si = None
        sj = None
        litter = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    si = i
                    sj = j
                elif classroom[i][j] == "L":
                    litter.append((i, j))
        litter_to_index = {}
        for li, (i, j) in enumerate(litter):
            litter_to_index[(i, j)] = li
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque([(si, sj)])
        visited = [[False] * n for _ in range(m)]
        visited[si][sj] = True
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if (
                    0 <= ni < m
                    and 0 <= nj < n
                    and not visited[ni][nj]
                    and classroom[ni][nj] != "X"
                ):
                    queue.append((ni, nj))
                    visited[ni][nj] = True
        for i, j in litter:
            if not visited[i][j]:
                return -1
        queue = deque([(si, sj, energy, 0, 0)])
        distances = {(si, sj, energy, 0): 0}
        l = len(litter)
        completed_bitmask = (1 << l) - 1
        while queue:
            i, j, energy_left, bitmask, distance = queue.popleft()
            if bitmask == completed_bitmask:
                return distance
            elif energy_left == 0:
                continue
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if classroom[ni][nj] == "X":
                        continue
                    new_energy_left = energy_left - 1
                    if classroom[ni][nj] == "R":
                        new_energy_left = energy
                    new_bitmask = bitmask
                    if classroom[ni][nj] == "L":
                        new_bitmask |= 1 << litter_to_index[(ni, nj)]
                    if (ni, nj, new_energy_left, new_bitmask) not in distances:
                        new_distance = distance + 1
                        if new_bitmask == completed_bitmask:
                            return new_distance
                        distances[(ni, nj, new_energy_left, new_bitmask)] = new_distance
                        queue.append(
                            (ni, nj, new_energy_left, new_bitmask, new_distance)
                        )
        return -1
