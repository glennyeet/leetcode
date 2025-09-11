class Solution:
    def sortVowels(self, s: str) -> str:
        # Sorting: O(n) time, O(n) space, where n is the size of s

        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        vowel_positions = []
        s_vowels = []
        for i, c in enumerate(s):
            if c in vowels:
                vowel_positions.append(i)
                s_vowels.append(c)
        s_vowels.sort()
        sorted_s = list(s)
        for pos, vowel in zip(vowel_positions, s_vowels):
            sorted_s[pos] = vowel
        return "".join(sorted_s)
