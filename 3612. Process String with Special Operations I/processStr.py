class Solution:
    def processStr(self, s: str) -> str:
        # Simulation: O(2^n) time, O(2^n)
        # space, where n is the size of s

        result = []
        for char in s:
            if char.islower():
                result.append(char)
            elif char == "*" and result:
                result.pop()
            elif char == "#":
                result *= 2
            elif char == "%":
                result.reverse()
        return "".join(result)
