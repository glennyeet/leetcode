class Solution:
    def totalMoney(self, n: int) -> int:
        # Simulation: O(n) time, O(1) space

        def find_triangular_number(t: int) -> int:
            return t * (t + 1) // 2

        days_left = n
        weeks_elapsed = 0
        total = 0
        while days_left:
            days_used = min(days_left, 7)
            days_left -= days_used
            total += find_triangular_number(
                days_used + weeks_elapsed
            ) - find_triangular_number(weeks_elapsed)
            weeks_elapsed += 1
        return total
