from functools import cache


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # Top-down DP: O(nt) time, O(nt) space

        n = len(words)
        w = len(words[0])
        t = len(target)
        mod_factor = 10**9 + 7

        @cache
        def count_char_ways(word_index: int, char: str) -> int:
            ways = 0
            for i in range(n):
                if words[i][word_index] == char:
                    ways += 1
            return ways

        @cache
        def count_ways(word_index: int, target_index: int) -> int:
            if target_index == t:
                return 1
            elif word_index == w:
                return 0
            ways = 0
            ways += count_char_ways(word_index, target[target_index]) * count_ways(
                word_index + 1, target_index + 1
            )
            ways %= mod_factor
            ways += count_ways(word_index + 1, target_index)
            ways %= mod_factor
            return ways

        return count_ways(0, 0)
