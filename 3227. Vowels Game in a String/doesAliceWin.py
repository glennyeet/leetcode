class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Math: O(n) time, O(1) space, where n is the size of s

        vowels = ["a", "e", "i", "o", "u"]
        total_vowels = 0
        for char in s:
            total_vowels += char in vowels
        return (total_vowels % 2 == 0 and total_vowels > 0) or total_vowels % 2 == 1
