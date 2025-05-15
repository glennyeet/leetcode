from typing import List


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # Linear Algebra: O(n + log(t)) time, O(1) space, where n is the size
        # of s

        mod_factor = 10**9 + 7
        identity = [[0] * 26 for _ in range(26)]
        for i in range(len(identity)):
            identity[i][i] = 1

        def matrix_multiplication(
            a: list[list[int]], b: list[list[int]]
        ) -> list[list[int]]:
            a_rows = len(a)
            a_cols = len(a[0])
            b_cols = len(b[0])
            c = [[0] * b_cols for _ in range(a_rows)]
            for i in range(a_rows):
                for j in range(a_cols):
                    for k in range(b_cols):
                        c[i][k] += a[i][j] * b[j][k]
            for i in range(a_rows):
                for j in range(b_cols):
                    c[i][j] %= mod_factor
            return c

        def matrix_power(a: list[list[int]], power: int) -> int:
            if power == 0:
                return identity
            elif power == 1:
                return a
            a_t_half = matrix_power(a, power // 2)
            if power % 2:
                return matrix_multiplication(
                    matrix_multiplication(a_t_half, a_t_half), a
                )
            else:
                return matrix_multiplication(a_t_half, a_t_half)

        character_counter = [[0] * 26]
        for char in s:
            character_counter[0][ord(char) - ord("a")] += 1
        a = [[0] * 26 for _ in range(26)]
        for i, transformations in enumerate(nums):
            for j in range(transformations):
                a[i][(i + j + 1) % 26] += 1
        x_t = matrix_multiplication(character_counter, matrix_power(a, t))
        return sum(x_t[0]) % mod_factor
