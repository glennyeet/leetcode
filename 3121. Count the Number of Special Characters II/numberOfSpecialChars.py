class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Hash Table: O(n) time, O(1) space

        uppercase_count = [0] * 26
        lowercase_count = [0] * 26
        special_letters = set()
        for char in word:
            if ord(char) <= 90:
                char_index = ord(char) - ord("A")
                uppercase_count[char_index] += 1
            else:
                char_index = ord(char) - ord("a")
                lowercase_count[char_index] += 1
            uppercase_char = char.upper()
            lowercase_char = char.lower()
            if (
                char == uppercase_char
                and uppercase_char not in special_letters
                and uppercase_count[char_index] == 1
                and lowercase_count[char_index]
            ):
                special_letters.add(uppercase_char)
            elif char == lowercase_char and uppercase_char in special_letters:
                special_letters.remove(uppercase_char)
        return len(special_letters)
