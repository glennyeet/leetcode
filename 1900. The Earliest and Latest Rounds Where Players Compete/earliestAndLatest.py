from typing import List


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        # Top-down DP: O(2^n) time, O(2^n) space

        first_player = firstPlayer - 1
        second_player = secondPlayer - 1
        players = []
        for i in range(n):
            players.append(i)
        earliest_round = float("inf")
        latest_round = float("-inf")

        def calculate_round_result(players: list[int], current_round: int) -> None:
            p = len(players)
            for i in range(p // 2):
                if (players[i], players[p - i - 1]) in [
                    (first_player, second_player),
                    (second_player, first_player),
                ]:
                    nonlocal earliest_round
                    earliest_round = min(earliest_round, current_round)
                    nonlocal latest_round
                    latest_round = max(latest_round, current_round)
                    return
            matches = p // 2
            if not p % 2:
                matches -= 2
            else:
                if players[p // 2] in [first_player, second_player]:
                    matches -= 1
                else:
                    matches -= 2
            for i in range(1 << matches):
                new_players = []
                match_results = i
                for j in range(p // 2):
                    if players[j] in [first_player, second_player]:
                        new_players.append(players[j])
                        continue
                    if players[p - j - 1] in [first_player, second_player]:
                        new_players.append(players[p - j - 1])
                        continue
                    if match_results & 1:
                        new_players.append(players[p - j - 1])
                    else:
                        new_players.append(players[j])
                    match_results >>= 1
                if p % 2:
                    new_players.append(players[p // 2])
                new_players.sort()
                calculate_round_result(new_players, current_round + 1)

        calculate_round_result(players, 1)
        return [earliest_round, latest_round]
