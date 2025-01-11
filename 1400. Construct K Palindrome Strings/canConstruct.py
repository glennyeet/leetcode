from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Hash map: O(n) time, O(n) space

        n = len(s)
        if n < k:
            return False
        elif n == k:
            return True
        counter = Counter(s)
        odd_char_counts = 0
        for char in counter:
            if counter[char] % 2:
                odd_char_counts += 1
        if odd_char_counts > k:
            return False
        return True
