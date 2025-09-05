class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # Enumeration + Bit Manipulation: O(log(max(num1, num2))) time, O(1) space

        for i in range(61):
            powers_of_two_sum = num1 - i * num2
            if powers_of_two_sum.bit_count() <= i <= powers_of_two_sum:
                return i
        return -1
