class Solution:
    def maxScore(self, s: str) -> int:
        # Prefix sum: O(n) time, O(1) space

        n = len(s)
        ones = 0
        for char in s:
            if char == "1":
                ones += 1
        left_score = 0
        right_score = ones
        max_score = 0
        for i in range(n - 1):
            if s[i] == "0":
                left_score += 1
            else:
                right_score = max(right_score - 1, 0)
            max_score = max(max_score, left_score + right_score)
        return max_score
