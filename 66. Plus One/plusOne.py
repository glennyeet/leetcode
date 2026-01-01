from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Math: O(n) time, O(n) space, where n is the
        # size of digits

        n = len(digits)
        result = []
        ones_digit = digits[-1] + 1
        carry = 0
        if ones_digit > 9:
            ones_digit -= 10
            carry = 1
        result.append(ones_digit)
        i = n - 2
        while i >= 0 or carry:
            if i < 0:
                result.append(carry)
                carry = 0
            else:
                digit = digits[i] + carry
                if digit > 9:
                    digit -= 10
                else:
                    carry = 0
                result.append(digit)
                i -= 1
        result.reverse()
        return result
