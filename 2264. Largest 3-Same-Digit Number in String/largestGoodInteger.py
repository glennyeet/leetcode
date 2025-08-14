class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Brute Force: O(n) time, O(1) space

        streak = 0
        max_good_int = ""
        for i, digit in enumerate(num):
            if i == 0 or digit == num[i - 1]:
                streak += 1
            else:
                streak = 1
            if streak >= 3:
                max_good_int = max(max_good_int, digit * 3)
        return max_good_int
