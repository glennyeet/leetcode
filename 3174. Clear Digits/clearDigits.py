class Solution:
    def clearDigits(self, s: str) -> str:
        # Stack: O(n) time, O(n) space,
        # where n is the length of s

        letter_stack = []
        for char in s:
            if str.isalpha(char):
                letter_stack.append(char)
            else:
                letter_stack.pop()
        return "".join(letter_stack)
