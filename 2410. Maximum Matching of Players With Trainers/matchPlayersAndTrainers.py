from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        m = len(trainers)
        sorted_players = sorted(players)
        sorted_trainers = sorted(trainers)
        max_matchings = 0
        j = 0
        for ability in sorted_players:
            while j < m:
                if ability <= sorted_trainers[j]:
                    max_matchings += 1
                    j += 1
                    break
                j += 1
            if j == m:
                break
        return max_matchings
