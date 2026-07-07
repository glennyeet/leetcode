class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # String: O(log(n)) time, O(log(n)) space

        n_sum = 0
        if n == 0:
            x = 0
        else:
            n_digits = list(str(n))
            x = []
            for digit in n_digits:
                if digit != "0":
                    x.append(digit)
                    n_sum += int(digit)
            x = int("".join(x))
        return x * n_sum
