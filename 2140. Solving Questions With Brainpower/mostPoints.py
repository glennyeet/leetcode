from typing import List
# from functools import cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Top-down DP: O(n) time, O(n) space

        # n = len(questions)

        # @cache
        # def get_max_points(start: int) -> int:
        #     if start >= n:
        #         return 0
        #     points, brainpower = questions[start]
        #     return max(
        #         points + get_max_points(start + brainpower + 1),
        #         get_max_points(start + 1),
        #     )

        # return get_max_points(0)

        # Bottom-up DP: O(n) time, O(n) space

        n = len(questions)
        max_points = [0] * n
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            solve_points = points
            next_question = i + brainpower + 1
            if next_question < n:
                solve_points += max_points[next_question]
            skip_points = 0
            next_question = i + 1
            if next_question < n:
                skip_points += max_points[next_question]
            max_points[i] = max(solve_points, skip_points)
        return max_points[0]
