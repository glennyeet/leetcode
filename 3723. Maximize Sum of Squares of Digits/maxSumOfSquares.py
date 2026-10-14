class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Greedy: O(n) time, O(n) space, where n is num

        max_score_good_integer = []
        sum_left = sum
        for _ in range(num):
            digit = min(sum_left, 9)
            max_score_good_integer.append(str(digit))
            sum_left -= digit
        if sum_left:
            return ""
        max_score_good_integer = "".join(max_score_good_integer)
        return max_score_good_integer
