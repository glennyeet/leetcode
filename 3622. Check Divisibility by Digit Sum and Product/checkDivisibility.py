class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Math: O(log(n)) time, O(1) space

        digit_sum = 0
        digit_product = 1
        cur_n = n
        while cur_n:
            digit = cur_n % 10
            cur_n //= 10
            digit_sum += digit
            digit_product *= digit
        return n % (digit_sum + digit_product) == 0
