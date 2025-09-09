from collections import defaultdict


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Line Sweep: O(n) time, O(n) space

        mod_factor = 10**9 + 7
        secret_knowers = 1
        delay_end = defaultdict(int)
        delay_end[1 + delay] += 1
        forget_start = defaultdict(int)
        forget_start[1 + forget] += 1
        secret_sharers = 0
        for i in range(1, n + 1):
            secret_knowers -= forget_start[i]
            secret_sharers -= forget_start[i]
            secret_sharers += delay_end[i]
            secret_sharers %= mod_factor
            secret_knowers += secret_sharers
            secret_knowers %= mod_factor
            delay_end[i + delay] += secret_sharers
            forget_start[i + forget] += secret_sharers
        return secret_knowers
