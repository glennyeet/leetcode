from itertools import permutations


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # Backtracking: O(d!) time, O(d) space, where d is the number of
        # digits in n

        total_digits = len(str(n))
        min_num = float("inf")

        def find_min_num(digits_left: int, d: int, digits: list[str]) -> None:
            nonlocal min_num
            if digits_left == 0:
                for num in permutations(digits):
                    num = int("".join(num))
                    if num > n and num < min_num:
                        min_num = num
            if digits_left >= d:
                find_min_num(digits_left - d, d + 1, digits + [str(d)] * d)
            if digits_left >= d + 1:
                find_min_num(digits_left, d + 1, digits)

        find_min_num(total_digits, 1, [])
        if min_num == float("inf"):
            find_min_num(total_digits + 1, 1, [])
        return min_num
