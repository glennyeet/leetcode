from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where n
        # is the size of answers

        answers_counter = Counter(answers)
        min_rabbits = 0
        for answer, count in answers_counter.items():
            min_rabbits += (count + answer) // (answer + 1) * (answer + 1)
        return min_rabbits
