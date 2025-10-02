class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Simulation: O(sqrt(b)) time, O(1) space

        full_bottles = numBottles
        exchange_cost = numExchange
        empty_bottles = 0
        max_drinks = 0
        while full_bottles:
            max_drinks += full_bottles
            empty_bottles += full_bottles
            full_bottles = 0
            while empty_bottles >= exchange_cost:
                empty_bottles -= exchange_cost
                full_bottles += 1
                exchange_cost += 1
        return max_drinks
