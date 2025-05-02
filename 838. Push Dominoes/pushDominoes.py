class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Prefix Sum: O(n) time, O(n) space

        n = len(dominoes)
        left = [float("inf")] * n
        for i in reversed(range(n)):
            if dominoes[i] == "L":
                left[i] = 0
            elif dominoes[i] == "." and i < n - 1:
                left[i] = left[i + 1] + 1
        right = [float("inf")] * n
        for i in range(n):
            if dominoes[i] == "R":
                right[i] = 0
            elif dominoes[i] == "." and i > 0:
                right[i] = right[i - 1] + 1
        final_state = [None] * n
        for i in range(n):
            if left[i] < right[i]:
                final_state[i] = "L"
            elif left[i] > right[i]:
                final_state[i] = "R"
            else:
                final_state[i] = "."
        return "".join(final_state)
