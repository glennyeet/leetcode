class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        for c in s:
            if c == "]" and stack:
                stack -= 1
            else:
                stack += 1
        return stack // 2
