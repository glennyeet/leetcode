class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # O(n^2) runtime

        # if len(s) != len(goal):
        #     return False
        # first_char = goal[0]
        # occurrences = []
        # for i, c in enumerate(s):
        #     if c == first_char:
        #         occurences.append(i)
        # for i in occurrences:
        #     shifted_s = s[i:] + s[:i]
        #     if shifted_s == goal:
        #         return True
        # return False

        # O(n) runtime

        double_s = s + s
        return len(s) == len(goal) and goal in double_s
