class MinStack:
    # Stack

    def __init__(self):
        # O(1) time, O(1) space

        self.stack = []
        self.min_elements = []

    def push(self, val: int) -> None:
        # O(1) time, O(1) space

        self.stack.append(val)
        if not self.min_elements:
            self.min_elements.append(val)
        else:
            self.min_elements.append(min(self.min_elements[-1], val))

    def pop(self) -> None:
        # O(1) time, O(1) space

        self.stack.pop()
        self.min_elements.pop()

    def top(self) -> int:
        # O(1) time, O(1) space

        return self.stack[-1]

    def getMin(self) -> int:
        # O(1) time, O(1) space

        return self.min_elements[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
