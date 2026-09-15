class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # Greedy: O(n * k + n * log(n)) time, O(n) space

        n = len(s)
        palindrome_intervals = []
        for i in range(n - k + 1):
            for j in range(i + k, i + k + 2):
                if s[i:j] == s[i:j][::-1]:
                    palindrome_intervals.append((i, j - 1))
        palindrome_intervals.sort(key=lambda i: i[1])
        max_substrings = 0
        next_start = -1
        for start, end in palindrome_intervals:
            if start >= next_start:
                max_substrings += 1
                next_start = end + 1
        return max_substrings
