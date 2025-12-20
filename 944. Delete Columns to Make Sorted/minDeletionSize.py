from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # String: O(n * c) time, O(c) space, where c is the
        # length of a string in strs

        n = len(strs)
        total_columns = len(strs[0])
        is_sorted = [True] * total_columns
        for i in range(1, n):
            for j in range(total_columns):
                if is_sorted[j] and strs[i][j] < strs[i - 1][j]:
                    is_sorted[j] = False
        return is_sorted.count(False)
