from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Hash Table + Simulation: O(n) time, O(m) space, where n is the size
        # of commands and m is the size of obstacles

        obstacles_set = set()
        for x, y in obstacles:
            obstacles_set.add((x, y))
        max_distance = 0
        cur_x = 0
        cur_y = 0
        cur_direction = 0  # N, E, S, W
        for command in commands:
            if command == -2:
                cur_direction = (cur_direction - 1) % 4
            elif command == -1:
                cur_direction = (cur_direction + 1) % 4
            else:
                for _ in range(command):
                    if cur_direction == 0:
                        if (cur_x, cur_y + 1) in obstacles_set:
                            break
                        cur_y += 1
                    elif cur_direction == 1:
                        if (cur_x + 1, cur_y) in obstacles_set:
                            break
                        cur_x += 1
                    elif cur_direction == 2:
                        if (cur_x, cur_y - 1) in obstacles_set:
                            break
                        cur_y -= 1
                    else:
                        if (cur_x - 1, cur_y) in obstacles_set:
                            break
                        cur_x -= 1
                max_distance = max(max_distance, cur_x**2 + cur_y**2)
        return max_distance
