from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        # Simulation + Stack: O(n * log(n)) time, O(n) space, where n is the
        # size of positions.

        robots = []
        for i, (position, direction) in enumerate(zip(positions, directions)):
            robots.append((position, i, direction))
        robots.sort()
        right_moving_robots = []
        cur_healths = healths.copy()
        for _, i, direction in robots:
            if direction == "R":
                right_moving_robots.append(i)
            elif right_moving_robots:
                while right_moving_robots and cur_healths[i] > 0:
                    j = right_moving_robots.pop()
                    if cur_healths[i] > cur_healths[j]:
                        cur_healths[i] -= 1
                        cur_healths[j] = 0
                    elif cur_healths[i] < cur_healths[j]:
                        cur_healths[i] = 0
                        cur_healths[j] -= 1
                        right_moving_robots.append(j)
                    else:
                        cur_healths[i] = 0
                        cur_healths[j] = 0
        remaining_robots = []
        for health in cur_healths:
            if health > 0:
                remaining_robots.append(health)
        return remaining_robots
