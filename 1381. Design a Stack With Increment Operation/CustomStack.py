# O(k) increment
# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.stack = []
#         self.max_size = maxSize

#     def push(self, x: int) -> None:
#         if len(self.stack) != self.max_size:
#             self.stack.append(x)

#     def pop(self) -> int:
#         if not len(self.stack):
#             return -1
#         return self.stack.pop()

#     def increment(self, k: int, val: int) -> None:
#         if k < len(self.stack):
#             unchanged_elements = []
#             for _ in range(len(self.stack) - k):
#                 unchanged_elements.append(self.stack.pop())
#             for i in range(len(self.stack)):
#                 self.stack[i] += val
#             for _ in range(len(unchanged_elements)):
#                 self.stack.append(unchanged_elements.pop())
#         else:
#             for i in range(len(self.stack)):
#                 self.stack[i] += val


# O(1) increment
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.increments = [0] * maxSize
        self.top = -1
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if self.top < self.max_size - 1:
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top == -1:
            return -1
        value = self.stack[self.top] + self.increments[self.top]
        if self.top > 0:
            self.increments[self.top - 1] += self.increments[self.top]
        self.increments[self.top] = 0
        self.top -= 1
        return value

    def increment(self, k: int, val: int) -> None:
        if self.top >= 0:
            k_index = min(k - 1, self.top)
            self.increments[k_index] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
