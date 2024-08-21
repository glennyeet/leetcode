class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        cache = [[0] * n for _ in range(n)]

        def get_min(left: int, right: int) -> int:
            if left == right:
                return 1
            elif left > right:
                return 0
            elif cache[left][right]:
                return cache[left][right]
            best = get_min(left, left) + get_min(left + 1, right)
            for i in range(left + 1, right + 1):
                if s[left] == s[i]:
                    best = min(best, get_min(left, i - 1) + get_min(i + 1, right))
            cache[left][right] = best
            return best

        return get_min(0, n - 1)
