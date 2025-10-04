class Solution:
    def isPalindrome(self, s: str) -> bool:
        # String: O(n) time, O(n) space

        parsed_s = []
        for char in s:
            if char.isalnum():
                parsed_s.append(char.lower())
        parsed_s = "".join(parsed_s)
        return parsed_s == parsed_s[::-1]
