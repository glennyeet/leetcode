class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Prefix Sum: O(n) time, O(n) space

        open_penalties = [0]
        for traffic in customers:
            open_penalties.append(open_penalties[-1] + (traffic == "N"))
        close_penalties = [0]
        for traffic in reversed(customers):
            close_penalties.append(close_penalties[-1] + (traffic == "Y"))
        close_penalties.reverse()
        earliest_hour = 0
        min_penalty = float("inf")
        for i, (open_penalty, close_penalty) in enumerate(
            zip(open_penalties, close_penalties)
        ):
            total_penalty = open_penalty + close_penalty
            if total_penalty < min_penalty:
                earliest_hour = i
                min_penalty = total_penalty
        return earliest_hour
