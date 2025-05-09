from functools import cache


class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        # Top-down DP: O(n^2 * s) time, O(n^2 + nS) space,
        # where S is half the sum of the digits of num

        n = len(num)
        mod_factor = 10**9 + 7
        digits_counter = [0] * 10
        for digit in num:
            digits_counter[int(digit)] += 1
        factorial = [1]
        inverse_factorial = [pow(1, -1, mod_factor)]
        for i in range(1, n + 1):
            factorial.append(factorial[-1] * i % mod_factor)
            inverse_factorial.append(pow(factorial[-1], -1, mod_factor))
        if n % 2:
            numerator = factorial[(n + 1) // 2] * factorial[n // 2] % mod_factor
        else:
            numerator = factorial[n // 2] * factorial[n // 2] % mod_factor

        @cache
        def dp(index: int, delta_count: int, delta_sum: int) -> int:
            if index == 10:
                if delta_sum:
                    return 0
                if n % 2:
                    if delta_count == 1:
                        return 1
                    return 0
                else:
                    if not delta_count:
                        return 1
                    return 0
            denominator = 0
            for left in range(digits_counter[index] + 1):
                right = digits_counter[index] - left
                denominator += (
                    dp(
                        index + 1,
                        delta_count + (left - right),
                        delta_sum + (left - right) * index,
                    )
                    * inverse_factorial[left]
                    * inverse_factorial[right]
                )
                denominator %= mod_factor
            return denominator

        return numerator * dp(0, 0, 0) % mod_factor
