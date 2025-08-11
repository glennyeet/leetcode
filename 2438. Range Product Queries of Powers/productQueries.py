from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Bit Manipulation: O(qlog(b)) time, O(q) space, where q is the size
        # of queries and b is the number of bits in n

        powers = []
        power_of_two = 1
        while power_of_two <= n:
            if n & power_of_two:
                powers.append(power_of_two)
            power_of_two <<= 1
        mod_factor = 10**9 + 7
        answers = []
        for left, right in queries:
            answer = 1
            for i in range(left, right + 1):
                answer *= powers[i]
                answer %= mod_factor
            answers.append(answer)
        return answers
