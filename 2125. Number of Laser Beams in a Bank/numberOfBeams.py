from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Combinatorics: O(n) time, O(n) space, where n is
        # the size of bank

        ones_counts = []
        for row in bank:
            ones = row.count("1")
            if ones:
                ones_counts.append(ones)
        laser_beams = 0
        for i in range(len(ones_counts) - 1):
            laser_beams += ones_counts[i] * ones_counts[i + 1]
        return laser_beams
