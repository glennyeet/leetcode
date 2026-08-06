class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Enumeration: O(log(n)) time, O(1) space

        num = n
        while True:
            num_str = str(num)
            digit_product = 1
            for digit_str in num_str:
                digit = int(digit_str)
                digit_product *= digit
            if digit_product % t == 0:
                return num
            num += 1
