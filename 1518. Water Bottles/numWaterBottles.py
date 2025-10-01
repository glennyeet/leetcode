class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # Simulation: O(log_e(b)) time, O(1) space, where b is numBottles
        # and e is numExchange

        full_bottles = numBottles
        empty_bottles = 0
        drinks = 0
        while full_bottles:
            drinks += full_bottles
            empty_bottles += full_bottles
            full_bottles = empty_bottles // numExchange
            empty_bottles %= numExchange
        return drinks
