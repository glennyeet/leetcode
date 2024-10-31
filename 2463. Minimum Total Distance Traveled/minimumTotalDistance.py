from functools import cache
from math import inf


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        total_robots = len(robot)
        total_factories = len(factory)

        @cache
        def get_min_distance(robot_index: int, factory_index: int) -> int:
            if factory_index == total_factories:
                return inf
            min_distance = inf
            distance = 0
            for repair_slot in range(factory[factory_index][1] + 1):
                if robot_index + repair_slot == total_robots:
                    min_distance = min(min_distance, distance)
                    break
                min_distance = min(
                    min_distance,
                    distance
                    + get_min_distance(robot_index + repair_slot, factory_index + 1),
                )
                distance += abs(
                    robot[robot_index + repair_slot] - factory[factory_index][0]
                )
            return min_distance

        return get_min_distance(0, 0)
