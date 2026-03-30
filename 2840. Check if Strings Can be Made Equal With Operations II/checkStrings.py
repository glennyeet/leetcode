from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Hash Table: O(n) time, O(n) space

        if s1 == s2:
            return True
        n = len(s1)
        s1_even_chars = Counter()
        s1_odd_chars = Counter()
        s2_even_chars = Counter()
        s2_odd_chars = Counter()
        for i in range(n):
            if i % 2 == 0:
                s1_even_chars[s1[i]] += 1
                s2_even_chars[s2[i]] += 1
            else:
                s1_odd_chars[s1[i]] += 1
                s2_odd_chars[s2[i]] += 1
        return s1_even_chars == s2_even_chars and s1_odd_chars == s2_odd_chars
