from typing import List
from collections import Counter
from math import comb


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Hash Table + Math: O(n) time, O(n) space, where n is the size of points

        mod_factor = 10**9 + 7
        y_counter = Counter()
        for _, y in points:
            y_counter[y] += 1
        horizontal_sides = 0
        for y in y_counter:
            horizontal_sides = (
                horizontal_sides + comb(y_counter[y], 2) % mod_factor
            ) % mod_factor
        unique_horizontal_trapezoids = 0
        for y in y_counter:
            horizontal_sides_at_y = comb(y_counter[y], 2) % mod_factor
            unique_horizontal_trapezoids = (
                unique_horizontal_trapezoids
                + horizontal_sides_at_y * (horizontal_sides - horizontal_sides_at_y)
            ) % mod_factor
        return (unique_horizontal_trapezoids * pow(2, -1, mod_factor)) % mod_factor
