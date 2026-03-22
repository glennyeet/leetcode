from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Matrix: O(m * n) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        if mat == target:
            return True
        ninety_degree_mat = []
        for j in range(n):
            mat_row = []
            for i in range(m):
                mat_row.append(mat[i][j])
            ninety_degree_mat.append(list(reversed(mat_row)))
        if ninety_degree_mat == target:
            return True
        one_eighty_degree_mat = []
        for i in range(m):
            one_eighty_degree_mat.append(list(reversed(mat[i])))
        one_eighty_degree_mat.reverse()
        if one_eighty_degree_mat == target:
            return True
        two_seventy_degree_mat = []
        for j in range(n):
            mat_row = []
            for i in range(m):
                mat_row.append(mat[i][j])
            two_seventy_degree_mat.append(mat_row)
        two_seventy_degree_mat.reverse()
        return two_seventy_degree_mat == target
