from typing import List


class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        # Bottom-up DP: O(n^2 * w) time, O(n) space,
        # where w is the string in words with max
        # length

        n = len(words)

        def is_hamming_distance_one(a: str, b: str) -> bool:
            hamming_distance = 0
            for i in range(len(a)):
                hamming_distance += a[i] != b[i]
                if hamming_distance > 1:
                    return False
            return hamming_distance == 1

        dp = [1] * n
        prev_string = [-1] * n
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    groups[i] != groups[j]
                    and len(words[i]) == len(words[j])
                    and is_hamming_distance_one(words[i], words[j])
                    and dp[i] + 1 > dp[j]
                ):
                    dp[j] = dp[i] + 1
                    prev_string[j] = i
        max_index = 0
        for i in range(n):
            if dp[i] > dp[max_index]:
                max_index = i
        longest_subsequence = []
        while max_index != -1:
            longest_subsequence.append(words[max_index])
            max_index = prev_string[max_index]
        longest_subsequence.reverse()
        return longest_subsequence
