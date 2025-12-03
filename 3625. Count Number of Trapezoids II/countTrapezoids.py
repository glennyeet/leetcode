from typing import List
from collections import defaultdict, Counter
from math import gcd, comb


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Hash Table + Math: O(n^2) time, O(n^2) space

        n = len(points)
        sorted_points = sorted(points)
        line_groups = defaultdict(lambda: defaultdict(set))
        segment_groups = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
        for i in range(n):
            x1, y1 = sorted_points[i]
            for j in range(i + 1, n):
                x2, y2 = sorted_points[j]
                dx = x2 - x1
                dy = y2 - y1
                d_squared = dx**2 + dy**2
                gcd_m = gcd(abs(dx), abs(dy))
                dx //= gcd_m
                dy //= gcd_m
                m = (dy, dx)
                if dx == 0:
                    line_groups[0][x1].add(y1)
                    line_groups[0][x1].add(y2)
                    segment_groups[0][x1][d_squared].add((x1, y1, x2, y2))
                    continue
                if dy == 0:
                    line_groups[1][y1].add(x1)
                    line_groups[1][y1].add(x2)
                    segment_groups[1][y1][d_squared].add((x1, y1, x2, y2))
                    continue
                bx = y1 * dx - x1 * dy
                by = dx
                gcd_b = gcd(abs(bx), abs(by))
                bx //= gcd_b
                by //= gcd_b
                if bx < 0 and by < 0:
                    bx *= -1
                    by *= -1
                elif bx > 0 and by < 0:
                    bx *= -1
                    by *= -1
                b = (bx, by)
                line_groups[m][b].add(x1)
                line_groups[m][b].add(x2)
                segment_groups[m][b][d_squared].add((x1, y1, x2, y2))
        total_trapezoids = 0
        total_parallelograms = 0
        for m in line_groups:
            total_pairs = 0
            pair_counts = []
            for b in line_groups[m]:
                if len(line_groups[m][b]) >= 2:
                    pair_count = comb(len(line_groups[m][b]), 2)
                    pair_counts.append(pair_count)
                    total_pairs += pair_count
            if total_pairs == 0 or len(pair_counts) == 1:
                continue
            for pair_count in pair_counts:
                total_trapezoids += pair_count * (total_pairs - pair_count)
            segment_counter = Counter()
            for b in segment_groups[m]:
                for d_squared in segment_groups[m][b]:
                    segment_counter[d_squared] += len(segment_groups[m][b][d_squared])
            for b in segment_groups[m]:
                for d_squared in segment_groups[m][b]:
                    total_parallelograms += len(segment_groups[m][b][d_squared]) * (
                        segment_counter[d_squared]
                        - len(segment_groups[m][b][d_squared])
                    )
        return total_trapezoids // 2 - total_parallelograms // 4
