class Solution:
    def makeFancyString(self, s: str) -> str:
        # Brute Force: O(n) time, O(n) space,
        # where n is the size of s

        streak = 0
        streak_letter = s[0]
        fancy_string = []
        for letter in s:
            if letter == streak_letter:
                streak += 1
            else:
                streak = 1
                streak_letter = letter
            if streak < 3:
                fancy_string.append(letter)
        return "".join(fancy_string)
