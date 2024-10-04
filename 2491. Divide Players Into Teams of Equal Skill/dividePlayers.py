from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        n = len(skill)
        total_teams = n // 2
        if total_skill % total_teams == 1:
            return -1
        skill_counter = Counter(skill)
        team_skill = total_skill // total_teams
        teams = []
        for num in skill:
            second_num = team_skill - num
            if skill_counter[num] == 0 or skill_counter[second_num] == 0:
                continue
            skill_counter[num] -= 1
            skill_counter[second_num] -= 1
            teams.append((num, second_num))
        if len(teams) != total_teams:
            return -1
        chemistry = 0
        for p1, p2 in teams:
            chemistry += p1 * p2
        return chemistry
