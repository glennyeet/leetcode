class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Math: O(n * log(n)) time, O(1) space

        good_integers = 0
        good_digits = (0, 1, 8, 2, 5, 6, 9)
        new_num_digits = (2, 5, 6, 9)

        def is_good(num: int) -> bool:
            is_new_num = False
            while num != 0:
                digit = num % 10
                if digit not in good_digits:
                    return False
                if digit in new_num_digits:
                    is_new_num = True
                num //= 10
            return is_new_num

        for num in range(1, n + 1):
            if is_good(num):
                good_integers += 1
        return good_integers
