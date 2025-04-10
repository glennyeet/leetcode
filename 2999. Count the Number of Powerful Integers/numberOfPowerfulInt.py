from functools import cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Top-down DP: O(log(f)) time, O(log(f)) space, where f = finish

        def f(x: str) -> int:
            if int(x) < int(s):
                return 0
            padded_s = "-" * max(len(x) - len(s), 0) + s

            @cache
            def g(index: int, constrained: bool) -> int:
                if index == len(padded_s):
                    return 1
                powerful_integers = 0
                if constrained:
                    cur_digit = int(x[index])
                    if padded_s[index] == "-":
                        powerful_integers += min(cur_digit, limit + 1) * g(
                            index + 1, False
                        )
                        if cur_digit <= limit:
                            powerful_integers += g(index + 1, True)
                    else:
                        suffix_digit = int(padded_s[index])
                        if cur_digit == suffix_digit:
                            powerful_integers += g(index + 1, True)
                        elif cur_digit > suffix_digit:
                            powerful_integers += g(index + 1, False)
                else:
                    if padded_s[index] == "-":
                        powerful_integers += (limit + 1) * g(index + 1, False)
                    else:
                        powerful_integers += g(index + 1, False)
                return powerful_integers

            return g(0, True)

        return f(str(finish)) - f(str(start - 1))
