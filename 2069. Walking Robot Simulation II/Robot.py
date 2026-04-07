from typing import List


class Robot:
    # Simulation + Math: step() takes O(w + h) time, rest take O(1) time,
    # all takes O(1) space, where w is width and h is height

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.directions = ["East", "North", "West", "South"]
        self.direction_coords = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.cur_direction = 0

    def step(self, num: int) -> None:
        steps = num % ((self.width - 1 + self.height - 1) * 2)
        if steps == 0:
            steps += (self.width - 1 + self.height - 1) * 2
        for _ in range(steps):
            new_x = self.x + self.direction_coords[self.cur_direction][0]
            new_y = self.y + self.direction_coords[self.cur_direction][1]
            while not (0 <= new_x < self.width and 0 <= new_y < self.height):
                self.cur_direction = (self.cur_direction + 1) % 4
                new_x = self.x + self.direction_coords[self.cur_direction][0]
                new_y = self.y + self.direction_coords[self.cur_direction][1]
            self.x = new_x
            self.y = new_y

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.directions[self.cur_direction]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
