from math import inf


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        letter_counts = {"a": 0, "b": 0, "c": 0}
        for c in s:
            letter_counts[c] += 1
        if min(letter_counts.values()) < k:
            return -1
        min_minutes = inf
        l = 0
        for r, c in enumerate(s):
            letter_counts[c] -= 1
            while min(letter_counts.values()) < k:
                letter_counts[s[l]] += 1
                l += 1
            min_minutes = min(min_minutes, len(s) - (r - l + 1))
        return min_minutes
