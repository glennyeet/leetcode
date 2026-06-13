from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Simulation: O(w * c) time, O(w) space, where w is the size of
        # words and c is the max length of a string in words

        answer = []
        for word in words:
            weight = 0
            for char in word:
                weight += weights[ord(char) - ord("a")]
            weight %= 26
            answer.append(chr(ord("a") + (25 - weight)))
        return "".join(answer)
