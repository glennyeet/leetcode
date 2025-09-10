from typing import List


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        # Greedy + Hash Table: O(ln + fn) time, O(ln) space, where f is the
        # size of friendships

        l = len(languages)
        language_sets = [set()] * (l + 1)
        for i, user in enumerate(languages):
            language_sets[i + 1] = set(user)
        unintelligible_friendships = []
        for u, v in friendships:
            if not language_sets[u] & language_sets[v]:
                unintelligible_friendships.append((u, v))
        min_users = float("inf")
        for language in range(1, n + 1):
            users = 0
            taught_users = set()
            for u, v in unintelligible_friendships:
                if language not in language_sets[u] and u not in taught_users:
                    users += 1
                    taught_users.add(u)
                if language not in language_sets[v] and v not in taught_users:
                    users += 1
                    taught_users.add(v)
            min_users = min(min_users, users)
        return min_users
