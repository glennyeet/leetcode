from collections import Counter


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Hash map: O(m * n) time, O(m * n) space

        m = len(mat)
        n = len(mat[0])
        positions = {}
        for x in range(m):
            for y in range(n):
                positions[mat[x][y]] = (x, y)
        row_counter = Counter()
        col_counter = Counter()
        for i, num in enumerate(arr):
            x, y = positions[num]
            row_counter[x] += 1
            if row_counter[x] == n:
                return i
            col_counter[y] += 1
            if col_counter[y] == m:
                return i
