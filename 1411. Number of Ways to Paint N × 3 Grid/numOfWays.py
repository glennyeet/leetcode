from functools import cache


class Solution:
    def numOfWays(self, n: int) -> int:
        # Top-down DP: O(n) time, O(n) space

        mod_factor = 10**9 + 7
        possible_rows = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    for k in range(3):
                        if j != k:
                            possible_rows.append((i, j, k))
        possible_next_rows = []
        for i in range(len(possible_rows)):
            possible_next_rows.append([])
            for j in range(len(possible_rows)):
                is_valid_row = True
                for k in range(3):
                    if possible_rows[i][k] == possible_rows[j][k]:
                        is_valid_row = False
                        break
                if is_valid_row:
                    possible_next_rows[i].append(j)

        @cache
        def dp(i: int, prev_row: int) -> int:
            if i == n:
                return 1
            ways = 0
            for j in range(len(possible_next_rows[prev_row])):
                ways = (ways + dp(i + 1, j)) % mod_factor
            return ways

        total_ways = 0
        for i in range(len(possible_next_rows)):
            total_ways = (total_ways + dp(1, i)) % mod_factor
        return total_ways
