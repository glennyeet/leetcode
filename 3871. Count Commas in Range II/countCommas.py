class Solution:
    def countCommas(self, n: int) -> int:
        # Math: O(log(n)) time, O(1) space

        commas = 0
        i = 1000
        while i <= n:
            commas += n - i + 1
            i *= 1000
        return commas
