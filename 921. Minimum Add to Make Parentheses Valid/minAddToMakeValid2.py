class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Greedy: O(n) time, O(1) space, where
        # n is the size of s

        min_additions = 0
        open_brackets = 0
        for bracket in s:
            if bracket == "(":
                open_brackets += 1
            else:
                if open_brackets == 0:
                    min_additions += 1
                else:
                    open_brackets -= 1
        min_additions += open_brackets
        return min_additions
