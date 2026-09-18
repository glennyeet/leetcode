from collections import defaultdict
from string import ascii_lowercase


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Bottom-up DP: O(n) time, O(n) space

        n = len(s)
        first_index_of_char = {}
        last_index_of_char = {}
        for i, char in enumerate(s):
            if char not in first_index_of_char:
                first_index_of_char[char] = i
            last_index_of_char[char] = i
        cur_chars = set()
        is_inside_range = defaultdict(lambda: defaultdict(bool))
        for i, char1 in enumerate(s):
            if i == first_index_of_char[char1]:
                cur_chars.add(char1)
            if i == last_index_of_char[char1]:
                cur_chars.remove(char1)
            for char2 in cur_chars:
                is_inside_range[char1][char2] = True
        range_expanded = True
        while range_expanded:
            range_expanded = False
            for char1 in ascii_lowercase:
                for char2 in ascii_lowercase:
                    if (
                        char1 not in first_index_of_char
                        or char2 not in first_index_of_char
                        or first_index_of_char[char1] == first_index_of_char[char2]
                        and last_index_of_char[char1] == last_index_of_char[char2]
                    ):
                        continue
                    elif (
                        is_inside_range[char1][char2] and is_inside_range[char2][char1]
                    ):
                        first_index_of_char[char1] = min(
                            first_index_of_char[char1], first_index_of_char[char2]
                        )
                        first_index_of_char[char2] = min(
                            first_index_of_char[char1], first_index_of_char[char2]
                        )
                        last_index_of_char[char1] = max(
                            last_index_of_char[char1], last_index_of_char[char2]
                        )
                        last_index_of_char[char2] = max(
                            last_index_of_char[char1], last_index_of_char[char2]
                        )
                        range_expanded = True
        dp = [0] * n
        prev = [-1] * n
        for i, char in enumerate(s):
            dp[i] = dp[i - 1]
            prev[i] = i - 1
            if last_index_of_char[char] == i:
                if dp[first_index_of_char[char]] + 1 > dp[i]:
                    dp[i] = dp[first_index_of_char[char]] + 1
                    prev[i] = first_index_of_char[char] - 1
        i = n - 1
        substrings = []
        while prev[i] != -1:
            if dp[i] - dp[prev[i]] == 1:
                substrings.append(s[prev[i] + 1 : i + 1])
            i = prev[i]
        if dp[i] == 1 and prev[i] == -1:
            substrings.append(s[0 : i + 1])
        return substrings
