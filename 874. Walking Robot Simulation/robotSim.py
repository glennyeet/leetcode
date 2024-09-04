from collections import defaultdict


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def change_direction(self, curr_index: int, command: int) -> int:
        if command == -1:
            curr_index += 1
        elif command == -2:
            curr_index -= 1
        if curr_index < 0:
            return 3
        elif curr_index > 3:
            return 0
        return curr_index

    def get_euclidean_distance_squared(self, point: tuple[int, int]) -> int:
        return point[0] ** 2 + point[1] ** 2

    def get_obstance_dict(
        self, obstacles: list[list[int]]
    ) -> defaultdict[(int, int), bool]:
        obstacle_dict = defaultdict(bool)
        for obstacle in obstacles:
            obstacle_dict[(obstacle[0], obstacle[1])] = True
        return obstacle_dict

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction_index = 0
        curr_point = (0, 0)
        max_eds = 0
        obstacle_dict = self.get_obstance_dict(obstacles)
        for command in commands:
            if command < 0:
                direction_index = self.change_direction(direction_index, command)
            else:
                for _ in range(command):
                    dx = self.directions[direction_index][0]
                    dy = self.directions[direction_index][1]
                    new_point = (curr_point[0] + dx, curr_point[1] + dy)
                    if obstacle_dict[new_point]:
                        continue
                    curr_point = new_point
                    max_eds = max(
                        max_eds, self.get_euclidean_distance_squared(new_point)
                    )
        return max_eds
