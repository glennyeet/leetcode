from collections import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Hash Table: O(n) time, O(1) space

        n = len(s)
        left_letters = Counter()
        right_letters = Counter(s)
        palindromes = set()
        palindrome_count = 0
        for i in range(n):
            right_letters[s[i]] -= 1
            if i > 0:
                left_letters[s[i - 1]] += 1
            if i == 0 or i == n - 1:
                continue
            for j in range(26):
                border_letter = chr(ord("a") + j)
                possible_palindrome = border_letter + s[i] + border_letter
                if (
                    left_letters[border_letter] > 0
                    and right_letters[border_letter] > 0
                    and possible_palindrome not in palindromes
                ):
                    palindromes.add(possible_palindrome)
                    palindrome_count += 1
        return palindrome_count
