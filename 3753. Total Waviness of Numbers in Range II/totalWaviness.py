from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # Top-down DP: O(log(n)) time, O(log(n)) space, where n is the size of num2

        def count_waviness_up_to(x: int) -> int:
            x_str = str(x)
            n = len(x_str)

            @cache
            def dp(
                index: int,
                leading_zero: bool,
                is_tight: bool,
                prev_prev_digit: int,
                prev_digit: int,
            ) -> int:
                if index == n:
                    return 0
                total_waviness = 0
                if leading_zero:
                    total_waviness += dp(index + 1, True, False, -1, -1)
                if is_tight:
                    limit_digit = int(x_str[index])
                    for digit in range(limit_digit):
                        if digit == 0 and leading_zero:
                            continue
                        waviness = 0
                        if prev_prev_digit >= 0:
                            if prev_prev_digit < prev_digit and prev_digit > digit:
                                waviness += 1
                            elif prev_prev_digit > prev_digit and prev_digit < digit:
                                waviness += 1
                        waviness *= 10 ** (n - index - 1)
                        total_waviness += (
                            dp(
                                index + 1,
                                False,
                                False,
                                prev_digit,
                                digit,
                            )
                            + waviness
                        )
                    waviness = 0
                    if prev_prev_digit >= 0:
                        if prev_prev_digit < prev_digit and prev_digit > limit_digit:
                            waviness += 1
                        elif prev_prev_digit > prev_digit and prev_digit < limit_digit:
                            waviness += 1
                    waviness *= int("0" + x_str[index + 1 :]) + 1
                    total_waviness += (
                        dp(
                            index + 1,
                            False,
                            True,
                            prev_digit,
                            limit_digit,
                        )
                        + waviness
                    )
                    return total_waviness
                for digit in range(10):
                    if digit == 0 and leading_zero:
                        continue
                    waviness = 0
                    if prev_prev_digit >= 0:
                        if prev_prev_digit < prev_digit and prev_digit > digit:
                            waviness += 1
                        if prev_prev_digit > prev_digit and prev_digit < digit:
                            waviness += 1
                    waviness *= 10 ** (n - index - 1)
                    total_waviness += (
                        dp(
                            index + 1,
                            False,
                            False,
                            prev_digit,
                            digit,
                        )
                        + waviness
                    )
                return total_waviness

            return dp(0, True, True, -1, -1)

        return count_waviness_up_to(num2) - count_waviness_up_to(num1 - 1)
