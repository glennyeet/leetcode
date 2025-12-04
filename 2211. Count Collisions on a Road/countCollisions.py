class Solution:
    def countCollisions(self, directions: str) -> int:
        # Stack: O(n) time, O(n) space, where n is the size
        # of directions

        car_stack = []
        collisions = 0
        for direction in directions:
            if not car_stack:
                car_stack.append(direction)
                continue
            if direction == "L":
                if car_stack[-1] == "R":
                    car_stack.pop()
                    collisions += 2
                    while car_stack and car_stack[-1] == "R":
                        car_stack.pop()
                        collisions += 1
                    car_stack.append("S")
                elif car_stack[-1] == "S":
                    collisions += 1
            elif direction == "S":
                while car_stack and car_stack[-1] == "R":
                    car_stack.pop()
                    collisions += 1
                car_stack.append(direction)
            else:
                car_stack.append(direction)
        return collisions
