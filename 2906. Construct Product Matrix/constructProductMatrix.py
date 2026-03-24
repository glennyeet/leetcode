from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Prefix Sum: O(n * m) time, O(n * m) space

        n = len(grid)
        m = len(grid[0])
        mod_factor = 12345
        prefix_product = [1]
        for i in range(n):
            for j in range(m):
                prefix_product.append(prefix_product[-1] * grid[i][j] % mod_factor)
        suffix_product = [1]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                suffix_product.append(suffix_product[-1] * grid[i][j] % mod_factor)
        suffix_product.reverse()
        p = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                k = i * m + j
                p[i][j] = prefix_product[k] * suffix_product[k + 1] % mod_factor
        return p
