class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Minimax
        n = len(piles)
        cache = [[0] * ((n + 1) // 2 + 1) for _ in range(n + 1)]

        def get_max_delta(index: int, m: int) -> int:
            if index == n:
                return 0
            cached_best = cache[index][m]
            if cached_best > 0:
                return cached_best
            best = float("-inf")
            taken = 0
            for i in range(1, 2 * m + 1):
                if index + i - 1 >= n:
                    break
                taken += piles[index + i - 1]
                new_m = min(max(m, i), (n + 1) // 2)
                best = max(best, -get_max_delta(index + i, new_m) + taken)
            cache[index][m] = best
            return best

        total = sum(piles)
        max_delta = get_max_delta(0, 1)
        alice = (total + max_delta) // 2
        return alice
