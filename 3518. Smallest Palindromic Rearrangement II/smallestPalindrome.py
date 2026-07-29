from collections import Counter
from math import factorial
from string import ascii_lowercase


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Combinatronics + Hash Table: O(n) time, O(n) space

        n = len(s)
        m = n // 2
        char_counter = Counter(s[:m])
        base_permutation = factorial(m)
        for f in char_counter.values():
            base_permutation //= factorial(f)
        if k > base_permutation:
            return ""
        first_half = ""
        cur_k = k
        for i in range(m):
            for char in ascii_lowercase:
                if not char_counter[char]:
                    continue
                char_permutations = base_permutation * char_counter[char] // (m - i)
                if cur_k <= char_permutations:
                    char_counter[char] -= 1
                    first_half += char
                    base_permutation = char_permutations
                    break
                cur_k -= char_permutations
        if n % 2:
            return first_half + s[m] + first_half[::-1]
        else:
            return first_half + first_half[::-1]
