class Solution:
    def maximum69Number(self, num: int) -> int:
        # Brute Force: O(log(n)) time, O(log(n))
        # space, where n is num

        digits = list(str(num))
        for i, digit in enumerate(digits):
            if digit == "6":
                digits[i] = "9"
                break
        return int("".join(digits))
