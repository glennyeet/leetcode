class Solution:
    def minSteps(self, n: int) -> int:
        # def get_steps(curr: int, clipboard: int) -> int:
        #     if curr == n:
        #         return 0
        #     elif curr > n:
        #         return 1000
        #     elif (curr, clipboard) in cache:
        #         return cache[(curr, clipboard)]
        #     paste = 1 + get_steps(curr + clipboard, clipboard)
        #     copy_paste = 2 + get_steps(curr * 2, curr)
        #     steps = min(paste, copy_paste)
        #     cache[(curr, clipboard)] = steps
        #     return steps

        # if n == 1:
        #     return 0
        # return 1 + get_steps(1, 1)
        steps = [1000] * (n + 1)
        steps[1] = 0
        for i in range(2, n + 1):
            for j in range(1, n // 2 + 1):
                if i % j == 0:
                    steps[i] = min(steps[i], steps[j] + i // j)
        return steps[n]
