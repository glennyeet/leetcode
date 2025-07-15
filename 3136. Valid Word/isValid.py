class Solution:
    def isValid(self, word: str) -> bool:
        # Brute Force: O(n) time, O(1) space,
        # where n is the size of word

        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        has_vowel = False
        has_consonant = False
        for char in word:
            if has_vowel and has_consonant:
                break
            if char.isalpha():
                if char in "aeiouAEIOU":
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant
