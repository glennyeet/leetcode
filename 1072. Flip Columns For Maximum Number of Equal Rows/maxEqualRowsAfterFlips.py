from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = Counter()
        for row in matrix:
            row_key = []
            for bit in row:
                if row[0] == 0:
                    row_key.append(bit ^ 1)
                else:
                    row_key.append(bit)
            counter[tuple(row_key)] += 1
        return max(counter.values())
