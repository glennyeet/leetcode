from collections import deque
from string import ascii_lowercase


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Enumeration + Queue: O(n * (n / k)!) time, O((n / k)!) space,
        # where n is the size of s

        def check_subsequence(subsequence: str) -> bool:
            count = 0
            ss_index = 0
            for char in s:
                if char == subsequence[ss_index]:
                    ss_index += 1
                    if ss_index == len(subsequence):
                        ss_index = 0
                        count += 1
            return count >= k

        longest_subsequence = ""
        queue = deque([("", (1 << 26) - 1)])
        while queue:
            cur_subsequence, possible_chars = queue.popleft()
            if len(cur_subsequence) > len(longest_subsequence) or (
                len(cur_subsequence) == len(longest_subsequence)
                and cur_subsequence > longest_subsequence
            ):
                longest_subsequence = cur_subsequence
            new_chars = []
            for char in range(26):
                if 1 << char & possible_chars:
                    if check_subsequence(cur_subsequence + ascii_lowercase[char]):
                        new_chars.append(ascii_lowercase[char])
                    else:
                        possible_chars ^= 1 << char
            for char in new_chars:
                queue.append((cur_subsequence + char, possible_chars))
        return longest_subsequence
