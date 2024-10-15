class Solution:
    def minimumSteps(self, s: str) -> int:
        zeroes_count = 0
        for c in s:
            if c == "0":
                zeroes_count += 1
        if zeroes_count == 0 or zeroes_count == len(s):
            return 0
        ones_indexes = []
        for i, colour in enumerate(s[:zeroes_count]):
            if colour == "1":
                ones_indexes.append(i)
        steps = 0
        for i, colour in enumerate(s[zeroes_count:], zeroes_count):
            if colour == "0":
                steps += i - ones_indexes.pop()
        return steps
