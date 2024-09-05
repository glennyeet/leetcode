class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_left = (m + n) * mean - sum(rolls)
        if total_left <= 0 or total_left / n < 1 or total_left / n > 6:
            return []
        remainder = total_left % n
        observations = [total_left // n] * n
        i = 0
        while remainder > 0:
            observations[i] += 1
            remainder -= 1
            if i == n - 1:
                i = 0
            else:
                i += 1
        return observations
