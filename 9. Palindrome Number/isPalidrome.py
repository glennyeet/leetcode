class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return str(x) == str(x)[::-1]
        a = x
        b = 0
        while a > 0:
            b = b * 10 + a % 10
            a //= 10
        return x == b
