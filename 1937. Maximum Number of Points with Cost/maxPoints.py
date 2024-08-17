class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        total_points = [[-1] * n for _ in range(m)]
        for j in range(n):
            total_points[0][j] = points[0][j]
        for i in range(1, m):
            prev_row_max = -1
            for j in range(n):
                prev_row_max = max(prev_row_max - 1, total_points[i - 1][j])
                total_points[i][j] = prev_row_max + points[i][j]
            for j in range(n - 1, -1, -1):
                prev_row_max = max(prev_row_max - 1, total_points[i - 1][j])
                total_points[i][j] = max(
                    total_points[i][j], prev_row_max + points[i][j]
                )
        answer = -1
        for j in range(n):
            answer = max(answer, total_points[m - 1][j])
        return answer
