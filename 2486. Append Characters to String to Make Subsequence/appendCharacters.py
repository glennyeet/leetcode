class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t[0] not in s:
            return len(t)
        i = j = 0
        while i < len(s):
            if j >= len(t):
                return 0
            if s[i] == t[j]:
                j += 1
            i += 1
        chars = len(t) - j
        return chars
