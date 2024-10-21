class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def get_max_substrings(i: int, substrings: set) -> int:
            if i == len(s):
                return 0
            max_substrings = 0
            for j in range(i, len(s)):
                possible_substring = s[i : j + 1]
                if possible_substring not in substrings:
                    substrings.add(possible_substring)
                    max_substrings = max(
                        max_substrings, get_max_substrings(j + 1, substrings) + 1
                    )
                    substrings.remove(possible_substring)
                else:
                    continue
            return max_substrings

        return get_max_substrings(0, set())
