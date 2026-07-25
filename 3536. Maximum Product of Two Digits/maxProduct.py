class Solution:
    def maxProduct(self, n: int) -> int:
        # Math: O(log(n)) time, O(log(n)) space

        x = n
        digits_counter = [0] * 10
        while x:
            digits_counter[x % 10] += 1
            x //= 10
        digit1 = None
        digit2 = None
        for digit, count in reversed(list(enumerate(digits_counter))):
            if digit1 is None and count > 1:
                digit1 = digit
                digit2 = digit
                break
            if digit1 is None and count == 1:
                digit1 = digit
            elif count:
                digit2 = digit
                break
        return digit1 * digit2
