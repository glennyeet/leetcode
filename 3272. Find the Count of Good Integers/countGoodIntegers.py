from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Combinatorics: O(nlog(n) * 10^n) time, O(10^n) space

        good_integers = 0
        half_digits = (n + 1) // 2
        digit_combinations = set()
        permutations = []
        for i in range(n + 1):
            permutations.append(factorial(i))
        for i in range(10 ** (half_digits - 1), 10**half_digits):
            palindrome = str(i) + str(i)[::-1][n % 2 :]
            sorted_digits = "".join(sorted(palindrome))
            if sorted_digits in digit_combinations or int(palindrome) % k != 0:
                continue
            digit_combinations.add(sorted_digits)
            digit_counter = Counter(palindrome)
            combinations = (n - digit_counter["0"]) * permutations[n - 1]
            for count in digit_counter.values():
                combinations //= permutations[count]
            good_integers += combinations
        return good_integers
