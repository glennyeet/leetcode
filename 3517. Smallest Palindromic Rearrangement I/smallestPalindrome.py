class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # String: O(n) time, O(n) space, where n is
        # the size of s

        letter_counter = [0] * 26
        for char in s:
            letter_counter[ord(char) - ord("a")] += 1
        middle_char = None
        first_half = []
        for i, count in enumerate(letter_counter):
            char = chr(ord("a") + i)
            if count % 2 == 1:
                middle_char = char
            for _ in range(count // 2):
                first_half.append(char)
        palindrome = first_half.copy()
        if middle_char:
            palindrome.append(middle_char)
        for char in reversed(first_half):
            palindrome.append(char)
        return "".join(palindrome)
