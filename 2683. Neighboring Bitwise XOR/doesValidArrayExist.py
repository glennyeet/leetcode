class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Simulation: O(n) time, O(1) space, where n is the
        # size of derived

        last_value = 0
        for num in derived:
            last_value ^= num
        return last_value == 0
