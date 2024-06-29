class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(str(num))
        digits.sort()
        a = int(digits[0] + digits[3])
        b = int(digits[1] + digits[2])
        return a + b
