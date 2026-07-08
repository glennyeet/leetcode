from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # Prefix Sum + Math: O(m + q) time, O(m) space, where m is the size
        # of s and q is the size of queries

        mod_factor = 10**9 + 7
        prefix_sum = [0]
        prefix_x = [0]
        prefix_zeroes = [0]
        for char in s:
            prefix_sum.append(prefix_sum[-1] + int(char))
            zero = 0
            if char == "0":
                zero = 1
                prefix_x.append(prefix_x[-1])
            else:
                prefix_x.append((prefix_x[-1] * 10 + int(char)) % mod_factor)
            prefix_zeroes.append(prefix_zeroes[-1] + zero)
        answer = []
        for l, r in queries:
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]
            digits = r - l + 1
            offset = digits - (prefix_zeroes[r + 1] - prefix_zeroes[l])
            x = prefix_x[r + 1] - (
                (prefix_x[l] * pow(10, offset, mod_factor)) % mod_factor
            )
            answer.append((x * digit_sum) % mod_factor)
        return answer
