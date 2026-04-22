from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        # Brute Force: O(q * d * n) time, O(1) space, where q is the size of
        # queries and d is the size of dictionary

        n = len(queries[0])

        def can_edit(query: str, word: str) -> bool:
            hamming_dist = 0
            for i in range(n):
                hamming_dist += query[i] != word[i]
            return hamming_dist <= 2

        editable_queries = []
        for query in queries:
            for word in dictionary:
                if can_edit(query, word):
                    editable_queries.append(query)
                    break
        return editable_queries
