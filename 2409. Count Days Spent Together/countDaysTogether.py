class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        # Prefix Sum + Math: O(1) time, O(1) space

        days_of_the_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_elapsed = [0]
        for days in days_of_the_month:
            days_elapsed.append(days_elapsed[-1] + days)

        def find_day_of_the_year(date: str) -> int:
            date_month = int(date[:2])
            date_day = int(date[3:])
            return days_elapsed[date_month - 1] + date_day

        arrive_alice_day = find_day_of_the_year(arriveAlice)
        leave_alice_day = find_day_of_the_year(leaveAlice)
        arrive_bob_day = find_day_of_the_year(arriveBob)
        leave_bob_day = find_day_of_the_year(leaveBob)
        return max(
            0,
            min(leave_alice_day, leave_bob_day)
            - max(arrive_alice_day, arrive_bob_day)
            + 1,
        )
