class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Sliding Window + Enumeration: O(n * sqrt(n)) time, O(n) space

        n = len(s)
        next_zeroes = [n] * n
        for i in reversed(range(n - 1)):
            if s[i + 1] == "0":
                next_zeroes[i] = i + 1
            else:
                next_zeroes[i] = next_zeroes[i + 1]
        valid_substrings = 0
        for l in range(n):
            if s[l] == "0":
                zeroes = 1
            else:
                zeroes = 0
            r = l
            while zeroes**2 <= n:
                next_zero = next_zeroes[r]
                ones = (next_zero - l) - zeroes
                if ones >= zeroes**2:
                    valid_substrings += min(next_zero - r, ones - zeroes**2 + 1)
                r = next_zero
                zeroes += 1
                if r == n:
                    break
        return valid_substrings
