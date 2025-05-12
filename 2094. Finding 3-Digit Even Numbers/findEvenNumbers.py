from typing import List
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Brute Force: O(n) time, O(n) space, where n
        # is the size of digits

        digits_counter = Counter(digits)
        valid_integers = []
        for num in range(100, 1000, 2):
            num_counter = Counter()
            for digit in str(num):
                num_counter[int(digit)] += 1
            valid = True
            for digit in num_counter:
                if num_counter[digit] > digits_counter[digit]:
                    valid = False
            if valid:
                valid_integers.append(num)
        return valid_integers
