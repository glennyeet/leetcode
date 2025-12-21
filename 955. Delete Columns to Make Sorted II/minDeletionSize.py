from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Greedy: O(n * m) time, O(n * m) space

        n = len(strs)
        m = len(strs[0])
        min_deletions = 0
        read_substrings = [""] * n
        for i in range(m):
            is_valid_column = True
            for j in range(n - 1):
                if (
                    read_substrings[j] + strs[j][i]
                    > read_substrings[j + 1] + strs[j + 1][i]
                ):
                    is_valid_column = False
                    break
            if is_valid_column:
                for j in range(n):
                    read_substrings[j] += strs[j][i]
            else:
                min_deletions += 1
        return min_deletions
