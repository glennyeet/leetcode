class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Hash Table: O(n) time, O(1) space, where n
        # is the size of word

        uppercase_count = [0] * 26
        lowercase_count = [0] * 26
        special_letter_count = 0
        special_letters = set()

        for char in word:
            if ord(char) <= 90:
                char_index = ord(char) - ord("A")
                uppercase_count[char_index] += 1
            else:
                char_index = ord(char) - ord("a")
                lowercase_count[char_index] += 1
            if (
                char.lower() not in special_letters
                and uppercase_count[char_index]
                and lowercase_count[char_index]
            ):
                special_letter_count += 1
                special_letters.add(char.lower())
        return special_letter_count
