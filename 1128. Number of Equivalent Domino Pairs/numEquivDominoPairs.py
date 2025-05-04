from typing import List
from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Hash Map: O(n) time, O(n) space

        pairs = 0
        dominoes_counter = Counter()
        for top, bottom in dominoes:
            pair = tuple(sorted((top, bottom)))
            pairs += dominoes_counter[pair]
            dominoes_counter[pair] += 1
        return pairs
