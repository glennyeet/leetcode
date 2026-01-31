from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Array: O(n) time, O(1) space, where n is the size of letters

        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
