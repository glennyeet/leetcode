from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Hash Table + Enumeration: O(n^3) time, O(1) space

        n = len(digits)
        three_digit_even_numbers = set()
        for i in range(n):
            first_digit = digits[i]
            if first_digit == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                second_digit = digits[j]
                for k in range(n):
                    if k == j or k == i:
                        continue
                    third_digit = digits[k]
                    if third_digit % 2 == 1:
                        continue
                    three_digit_even_numbers.add(
                        first_digit * 100 + second_digit * 10 + third_digit
                    )

        return len(three_digit_even_numbers)
