from typing import List
from functools import cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @cache
        def get_min_score(v1: int, v3: int) -> int:
            if v1 + 1 == v3:
                return 0
            min_score = float("inf")
            for v2 in range(v1 + 1, v3):
                score = (
                    values[v1] * values[v2] * values[v3]
                    + get_min_score(v1, v2)
                    + get_min_score(v2, v3)
                )
                min_score = min(min_score, score)
            return min_score

        return get_min_score(0, n - 1)
