from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Hash Table + Backtracking: O(26^n) time, O(n^2) space

        n = len(bottom)
        levels = [list(bottom)]
        while len(levels) < n:
            levels.append([""] * (len(levels[-1]) - 1))
        allowed_dict = defaultdict(list)
        for pattern in allowed:
            b1, b2, b3 = list(pattern)
            allowed_dict[b1 + b2].append(b3)

        def can_build_pyramid(level: list[int], col: int) -> bool:
            if level == n:
                return True
            elif col >= len(levels[level]):
                return can_build_pyramid(level + 1, 0)
            bottom_blocks = levels[level - 1][col] + levels[level - 1][col + 1]
            for b3 in allowed_dict[bottom_blocks]:
                levels[level][col] = b3
                if can_build_pyramid(level, col + 1):
                    return True
                levels[level][col] = ""
            return False

        return can_build_pyramid(1, 0)
