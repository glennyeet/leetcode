from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # Prefix Sum: O(m * n) time, O(m) space, where n is the size
        # of mana

        m = len(skill)
        times = [0] * (m + 1)
        for mana_capacity in mana:
            time = 0
            max_time_delta = 0
            for i, wizard_skill in enumerate(skill):
                max_time_delta = max(max_time_delta, times[i + 1] - time)
                time += wizard_skill * mana_capacity
            time = max_time_delta
            for i, wizard_skill in enumerate(skill):
                time += wizard_skill * mana_capacity
                times[i + 1] = time
        return times[-1]
