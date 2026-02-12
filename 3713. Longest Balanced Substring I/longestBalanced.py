from collections import Counter


class Solution:
    def longestBalanced(self, s: str) -> int:
        # Hash Table + Enumeration: O(n^2) time, O(1) space

        n = len(s)
        max_length = 1
        for i in range(n):
            char_counter = Counter(s[i])
            for j in range(i + 1, n):
                char_counter[s[j]] += 1
                valid_count = char_counter[s[i]]
                for char in char_counter:
                    if char_counter[char] != valid_count:
                        break
                else:
                    max_length = max(max_length, j - i + 1)
        return max_length
