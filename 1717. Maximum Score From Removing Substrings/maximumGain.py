class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Greedy + Stack: O(n) time, O(n) space, where
        # n is the size of s

        if x < y:
            less_points_substring = "ab"
            less_points_value = x
            more_points_substring = "ba"
            more_points_value = y
        else:
            less_points_substring = "ba"
            less_points_value = y
            more_points_substring = "ab"
            more_points_value = x
        max_points = 0
        char_stack = []
        for char in s:
            char_stack.append(char)
            if (
                len(char_stack) >= 2
                and char_stack[-2] + char_stack[-1] == more_points_substring
            ):
                char_stack.pop()
                char_stack.pop()
                max_points += more_points_value
        remaining_s = "".join(char_stack)
        char_stack = []
        for char in remaining_s:
            char_stack.append(char)
            if (
                len(char_stack) >= 2
                and char_stack[-2] + char_stack[-1] == less_points_substring
            ):
                char_stack.pop()
                char_stack.pop()
                max_points += less_points_value
        return max_points
