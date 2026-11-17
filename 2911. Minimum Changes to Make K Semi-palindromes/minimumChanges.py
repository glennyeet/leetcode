from collections import defaultdict
from functools import cache


class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        # Sliding Window + Top-down DP: O(n^3) time, O(n^3) space

        n = len(s)
        chain_cost = {}
        for d in range(1, n):
            for centre in range(n):
                left = centre
                right = centre
                mismatches = 0
                while left >= 0 and right < n:
                    if s[left] != s[right]:
                        mismatches += 1
                    chain_cost[(left, right, d)] = mismatches
                    left -= d
                    right += d
            for centre in range(n):
                left = centre
                right = centre + d
                mismatches = 0
                while left >= 0 and right < n:
                    if s[left] != s[right]:
                        mismatches += 1
                    chain_cost[(left, right, d)] = mismatches
                    left -= d
                    right += d
        semi_palindrome_cost = defaultdict(lambda: float("inf"))
        for d in range(1, n):
            for start in range(n):
                chain_costs = [0] * d
                total_cost = 0
                for end in range(start + d, n):
                    chain = (end - start) % d
                    old_cost = chain_costs[chain]
                    chain_costs[chain] = chain_cost[(start + chain, end, d)]
                    total_cost += chain_costs[chain] - old_cost
                    length = end - start + 1
                    if length % d == 0 and length >= 2 * d:
                        semi_palindrome_cost[(start, end)] = min(
                            semi_palindrome_cost[(start, end)], total_cost
                        )

        @cache
        def dp(i, parts_left) -> float | int:
            if i >= n:
                if parts_left == 0:
                    return 0
                return float("inf")
            if parts_left == 0:
                return float("inf")
            min_letter_changes = float("inf")
            for j in range(i + 2, n + 1):
                min_letter_changes = min(
                    min_letter_changes,
                    dp(j, parts_left - 1) + semi_palindrome_cost[(i, j - 1)],
                )
            return min_letter_changes

        return dp(0, k)
