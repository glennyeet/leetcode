class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        while left < right:
            if s[left] < s[right]:
                s[right] = s[left]
            elif s[left] > s[right]:
                s[left] = s[right]
            left += 1
            right -= 1
        s = "".join(s)
        return s
