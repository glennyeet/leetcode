from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # Enumeration: O(1) time, O(1) space

        sequential_digit_numbers = []
        digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

        def find_sequential_digit_numbers(num_str: str) -> None:
            num = int(num_str)
            if num > high:
                return
            elif low <= num <= high:
                sequential_digit_numbers.append(num)
            next_digit_index = digits.index(num_str[-1]) + 1
            if next_digit_index < len(digits):
                find_sequential_digit_numbers(num_str + digits[next_digit_index])

        for digit in digits:
            find_sequential_digit_numbers(digit)
        sequential_digit_numbers.sort()
        return sequential_digit_numbers
