class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Stack: O(n) time, O(n) space

        n = len(s)
        if n % 2:
            return False
        unlocked_indices = []
        locked_indices = []
        for i, char in enumerate(s):
            if locked[i] == "0":
                unlocked_indices.append(i)
            elif char == "(":
                locked_indices.append(i)
            else:
                if locked_indices:
                    locked_indices.pop()
                elif unlocked_indices:
                    unlocked_indices.pop()
                else:
                    return False
        while (
            unlocked_indices
            and locked_indices
            and locked_indices[-1] < unlocked_indices[-1]
        ):
            unlocked_indices.pop()
            locked_indices.pop()
        if locked_indices:
            return False
        return True
