class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_len = len(n)
        if n_len == 1:
            palindrome = str(int(n) - 1)
            return palindrome

        def is_power_of_ten(n: int) -> bool:
            while n % 10 == 0:
                n //= 10
            return n == 1

        if is_power_of_ten(int(n)):
            palindrome = "9" * (n_len - 1)
            return palindrome

        def is_repeating_nines(n: str) -> bool:
            if n == "9" * n_len:
                return True
            return False

        if is_repeating_nines(n):
            palindrome = "1" + "0" * (n_len - 1) + "1"
            return palindrome

        def is_one_o_one(n: str) -> bool:
            if n == "11":
                return True
            zeroes = n[1 : n_len - 1]
            if n[0] == "1" and n[n_len - 1] == "1" and "0" * len(zeroes) == zeroes:
                return True
            return False

        if is_one_o_one(n):
            palindrome = "9" * (n_len - 1)
            return palindrome

        half_len = n_len // 2
        left_half = n[:half_len]
        has_even_digits = n_len % 2 == 0
        palindromes = []
        if has_even_digits:
            for delta in [-1, 0, 1]:
                new_left_half = str(int(left_half) + delta)
                palindromes.append(new_left_half + new_left_half[::-1])
        else:
            middle_digit = n[half_len]
            for delta in [-1, 0, 1]:
                if int(middle_digit) + delta >= 0:
                    new_middle_digit = str(int(middle_digit) + delta)
                    palindromes.append(left_half + new_middle_digit + left_half[::-1])
        n_int = int(n)
        min_diff = float("inf")
        palindrome = None
        for p in palindromes:
            if abs(int(p) - n_int) < min_diff and int(p) != n_int:
                min_diff = abs(int(p) - n_int)
                palindrome = p
            elif (
                abs(int(p) - n_int) == min_diff
                and int(p) != n_int
                and int(p) < int(palindrome)
            ):
                palindrome = p
        return palindrome
