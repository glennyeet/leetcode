class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) != self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        if not len(self.stack):
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k < len(self.stack):
            unchanged_elements = []
            for _ in range(len(self.stack) - k):
                unchanged_elements.append(self.stack.pop())
            for i in range(len(self.stack)):
                self.stack[i] += val
            for _ in range(len(unchanged_elements)):
                self.stack.append(unchanged_elements.pop())
        else:
            for i in range(len(self.stack)):
                self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
