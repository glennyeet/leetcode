from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # Bottom-up DP: O(n) time, O(n) space

        n = len(energy)
        total_energy = [0] * n
        for i in reversed(range(n)):
            if i + k >= n:
                total_energy[i] = energy[i]
            else:
                total_energy[i] = energy[i] + total_energy[i + k]
        return max(total_energy)
