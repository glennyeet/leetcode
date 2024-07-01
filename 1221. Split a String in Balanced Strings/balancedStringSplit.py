class Solution:
    def balancedStringSplit(self, s: str) -> int:
        max_strings = 0
        equilibrium = 0
        for c in s:
            if c == 'L':
                equilibrium += 1
            else:
                equilibrium -= 1
            if equilibrium == 0:
                max_strings += 1
        return max_strings
