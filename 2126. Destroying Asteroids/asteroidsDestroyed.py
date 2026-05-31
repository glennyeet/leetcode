from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Greedy: O(n * log(n)) time, O(n) space, where n is the size of
        # asteroids

        sorted_asteroids = sorted(asteroids)
        cur_mass = mass
        for asteroid_mass in sorted_asteroids:
            if cur_mass < asteroid_mass:
                return False
            cur_mass += asteroid_mass
        return True
