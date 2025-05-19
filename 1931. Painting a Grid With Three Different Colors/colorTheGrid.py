from collections import defaultdict


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # Bottom-up DP: O(n * 3^(2m)) time, O(n * 3^m) space

        mod_factor = 10**9 + 7

        def get_bitmask(num: int) -> list[int]:
            bitmask = []
            for _ in range(m):
                bitmask.append(num % 3)
                num //= 3
            return bitmask

        total_row_combinations = 3**m
        dp = [[0] * total_row_combinations for _ in range(n + 1)]
        valid_row_combos = []
        for combo in range(total_row_combinations):
            bitmask = get_bitmask(combo)
            is_valid = True
            for i in range(m - 1):
                if bitmask[i] == bitmask[i + 1]:
                    is_valid = False
            if is_valid:
                valid_row_combos.append(combo)
        valid_row_pairs = defaultdict(list)
        for prev_row_combo in valid_row_combos:
            prev_row_bitmask = get_bitmask(prev_row_combo)
            for cur_row_combo in valid_row_combos:
                cur_row_bitmask = get_bitmask(cur_row_combo)
                is_valid = True
                for prev_row_bit, cur_row_bit in zip(prev_row_bitmask, cur_row_bitmask):
                    if prev_row_bit == cur_row_bit:
                        is_valid = False
                if is_valid:
                    valid_row_pairs[prev_row_combo].append(cur_row_combo)
        for combo in valid_row_combos:
            dp[1][combo] = 1
        for row in range(2, n + 1):
            for prev_row_combo in valid_row_combos:
                for cur_row_combo in valid_row_pairs[prev_row_combo]:
                    dp[row][cur_row_combo] = (
                        dp[row][cur_row_combo] + dp[row - 1][prev_row_combo]
                    ) % mod_factor
        return sum(dp[n]) % mod_factor
