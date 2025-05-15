from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Greedy: O(n) time, O(n) space

        n = len(words)
        longest_subsequence = [words[0]]
        next_group = 1 - groups[0]
        for i in range(1, n):
            if groups[i] == next_group:
                longest_subsequence.append(words[i])
                next_group = 1 - groups[i]
        return longest_subsequence
