class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_letter = None
        count = 0
        fancy_string = ""
        for c in s:
            if c == prev_letter:
                count += 1
            else:
                prev_letter = c
                count = 1
            if count < 3:
                fancy_string += c
        return fancy_string
