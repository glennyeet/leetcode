from bisect import bisect_left
from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Greedy + Binary Search: O(n + log(n)) time, O(n) space, where n is the
        # size of s

        s_chars = set(s)
        used_chars = set()
        char_indices = defaultdict(list)
        for i, char in enumerate(s):
            char_indices[char].append(i)
        subsequence = []
        min_index = 0
        for _ in range(len(s_chars)):
            for char in ascii_lowercase:
                if char not in used_chars:
                    char_indices_index = bisect_left(char_indices[char], min_index)
                    if char_indices_index >= len(char_indices[char]):
                        continue
                    char_index = char_indices[char][char_indices_index]
                    is_valid_char = True
                    for s_char in s_chars:
                        if char == s_char:
                            continue
                        if s_char not in used_chars and bisect_left(
                            char_indices[s_char], char_index
                        ) >= len(char_indices[s_char]):
                            is_valid_char = False
                    if is_valid_char:
                        subsequence.append(char)
                        min_index = char_index + 1
                        used_chars.add(char)
                        break
        return "".join(subsequence)
