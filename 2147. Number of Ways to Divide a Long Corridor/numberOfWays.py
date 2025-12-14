class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Combinatorics: O(n) time, O(1) space, where n is the size of corridor

        mod_factor = 10**9 + 7
        total_seats = corridor.count("S")
        if total_seats == 0 or total_seats % 2 != 0:
            return 0
        current_seats = 0
        current_plants = float("-inf")
        divisions = 1
        for thing in corridor:
            if thing == "S":
                current_seats += 1
                if current_seats == 2:
                    current_seats = 0
                    current_plants = 0
                else:
                    if current_plants >= 0:
                        divisions = (divisions * (current_plants + 1)) % mod_factor
            else:
                current_plants += 1
        return divisions
