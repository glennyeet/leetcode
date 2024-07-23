class Solution:
    def minSwaps(self, s: str) -> int:
        i = 0
        stack = []
        while i < len(s):
            if s[i] == "]" and stack:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        swaps = (len(stack) + 1) // 2
        return swaps
