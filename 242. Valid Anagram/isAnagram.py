from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hash Table: O(s + t) time, O(s + t) space

        return Counter(s) == Counter(t)
