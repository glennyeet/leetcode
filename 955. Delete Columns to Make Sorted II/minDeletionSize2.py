from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Greedy: O(m * n) time, O(n) space

        n = len(strs)
        m = len(strs[0])
        min_deletions = 0
        word_is_sorted = [False] * (n - 1)
        for i in range(m):
            new_word_is_sorted = word_is_sorted[:]
            for j in range(n - 1):
                if not word_is_sorted[j]:
                    if strs[j][i] > strs[j + 1][i]:
                        min_deletions += 1
                        break
                    elif strs[j][i] < strs[j + 1][i]:
                        new_word_is_sorted[j] = True
            else:
                word_is_sorted = new_word_is_sorted
        return min_deletions
