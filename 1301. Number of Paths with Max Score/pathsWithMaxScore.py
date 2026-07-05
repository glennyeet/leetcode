from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # Bottom-up DP: O(n^2) time, O(n^2) space

        mod_factor = 10**9 + 7
        n = len(board)
        dp1 = [[-1] * n for _ in range(n)]
        dp1[-1][-1] = 0
        dp2 = [[0] * n for _ in range(n)]
        dp2[-1][-1] = 1
        directions = ((1, 0), (1, 1), (0, 1))
        for i1 in reversed(range(n)):
            for j1 in reversed(range(n)):
                if board[i1][j1] == "X" or i1 == n - 1 and j1 == n - 1:
                    continue
                max_sum = -1
                valid_paths = 0
                for di, dj in directions:
                    i2 = i1 + di
                    j2 = j1 + dj
                    if 0 <= i2 < n and 0 <= j2 < n and dp1[i2][j2] > -1:
                        if dp1[i2][j2] > max_sum:
                            max_sum = dp1[i2][j2]
                            valid_paths = dp2[i2][j2]
                        elif dp1[i2][j2] == max_sum:
                            valid_paths = (valid_paths + dp2[i2][j2]) % mod_factor
                if max_sum > -1:
                    if board[i1][j1].isdigit():
                        square_num = int(board[i1][j1])
                    else:
                        square_num = 0
                    dp1[i1][j1] = max_sum + square_num
                    dp2[i1][j1] = valid_paths
        if dp1[0][0] == -1:
            return [0, 0]
        return [dp1[0][0], dp2[0][0]]
