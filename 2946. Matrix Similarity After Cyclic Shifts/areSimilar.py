from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # Math: O(m * n) time, O(n) space

        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            if i % 2 == 0:
                new_start_index = n - k % n
            else:
                new_start_index = k % n
            shifted_row = mat[i][new_start_index:] + mat[i][:new_start_index]
            if shifted_row != mat[i]:
                return False
        return True
