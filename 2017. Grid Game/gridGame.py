from math import inf


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Prefix sum: O(n) time, O(n) space

        n = len(grid[0])
        prefix_sums1 = []
        sum1 = 0
        prefix_sums2 = []
        sum2 = 0
        for i in range(n):
            sum1 += grid[0][i]
            prefix_sums1.append(sum1)
            sum2 += grid[1][i]
            prefix_sums2.append(sum2)
        second_points = inf
        for i in range(n):
            points1 = sum1 - prefix_sums1[i]
            points2 = prefix_sums2[i] - grid[1][i]
            second_points = min(second_points, max(points1, points2))
        return second_points
