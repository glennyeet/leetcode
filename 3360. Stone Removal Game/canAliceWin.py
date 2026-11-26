class Solution:
    def canAliceWin(self, n: int) -> bool:
        # Simulation: O(1) time, O(1) space

        stones_left = n
        stones_to_remove = 10
        is_alices_turn = True
        while stones_left - stones_to_remove >= 0:
            stones_left -= stones_to_remove
            stones_to_remove -= 1
            is_alices_turn = not is_alices_turn
        return not is_alices_turn
