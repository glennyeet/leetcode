class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Backtracking: O(2^n * n) time, O(2^n) space, where n is the size of s

        n = len(s)
        valid_strings = set()

        def find_valid_strings(i: int, curr: list[str], depth: int) -> list[str]:
            if i == n:
                if depth == 0:
                    valid_strings.add("".join(curr))
                return
            if s[i] == "(":
                find_valid_strings(i + 1, curr, depth)
                curr.append("(")
                find_valid_strings(i + 1, curr, depth + 1)
                curr.pop()
            elif s[i] == ")":
                find_valid_strings(i + 1, curr, depth)
                if depth <= 0:
                    return
                curr.append(")")
                find_valid_strings(i + 1, curr, depth - 1)
                curr.pop()
            else:
                curr.append(s[i])
                find_valid_strings(i + 1, curr, depth)
                curr.pop()

        find_valid_strings(0, [], 0)
        max_len = 0
        for string in valid_strings:
            max_len = max(max_len, len(string))
        max_len_valid_strings = []
        for string in valid_strings:
            if len(string) == max_len:
                max_len_valid_strings.append(string)
        return max_len_valid_strings
