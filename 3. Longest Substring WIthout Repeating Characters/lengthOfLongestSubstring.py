class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, length = 0, 0
        usedChars = {}

        i, start = 0, 0
        for c in s:
            if c in usedChars:
                start = min(i, max(usedChars[c] + 1, start))
                length = i - start + 1
            else:
                length += 1
            usedChars[c] = i
            if length > maxLength:
                maxLength = length
            i += 1

        return maxLength
