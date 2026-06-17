class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Simulation: O(n) time, O(1) space,
        # where n is the size of s

        result_len = 0
        for char in s:
            if char.islower():
                result_len += 1
            elif result_len and char == "*":
                result_len -= 1
            elif char == "#":
                result_len *= 2
        if result_len <= k:
            return "."
        i = k
        cur_result_len = result_len
        for char in s[::-1]:
            if char.islower():
                cur_result_len -= 1
                if i == cur_result_len:
                    return char
            elif char == "*":
                cur_result_len += 1
            elif char == "#":
                cur_result_len //= 2
                if i >= cur_result_len:
                    i -= cur_result_len
            elif char == "%":
                i = cur_result_len - i - 1
        return "."
