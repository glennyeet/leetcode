from math import gcd


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Digit DP + Greedy: O(n + log^2(t)) time, O(n) space

        n = len(num)
        cur_t = t
        for i in range(2, 10):
            while cur_t % i == 0:
                cur_t //= i
        if cur_t > 1:
            return "-1"
        remaining_t = [0] * (n + 1)
        remaining_t[0] = t
        first_zero_index = n - 1
        num_digits = list(num)
        for i in range(n):
            if num_digits[i] == "0":
                first_zero_index = i
                break
            remaining_t[i + 1] = remaining_t[i] // gcd(
                remaining_t[i], int(num_digits[i])
            )
        if remaining_t[n] == 1:
            return num
        for i in reversed(range(first_zero_index + 1)):
            while True:
                num_digits[i] = chr(ord(num_digits[i]) + 1)
                if num_digits[i] > "9":
                    break
                t_now = remaining_t[i] // gcd(remaining_t[i], int(num_digits[i]))
                k = 9
                for j in reversed(range(i + 1, n)):
                    while t_now % k != 0:
                        k -= 1
                    t_now //= k
                    num_digits[j] = str(k)
                if t_now == 1:
                    return "".join(num_digits)
        ans = []
        cur_t = t
        for i in reversed(range(2, 10)):
            while cur_t % i == 0:
                ans.append(str(i))
                cur_t //= i
        ans_str = "".join(ans)
        padding = max(n + 1 - len(ans_str), 0)
        ans_str += "1" * padding
        return ans_str[::-1]
