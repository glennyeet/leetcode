from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Hash map: O(n) time, O(1) space

        left = set()
        right = Counter(s)
        palindromes = set()
        for mid_char in s:
            right[mid_char] -= 1
            for outer_char in left:
                if right[outer_char] > 0:
                    palindromes.add((outer_char, mid_char))
            left.add(mid_char)
        return len(palindromes)
