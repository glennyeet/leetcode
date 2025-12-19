from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Hash Table + BFS: O(n * log(n)) time, O(n) space

        meetings_dict = defaultdict(list)
        meetings_dict[0].append((0, firstPerson))
        for x, y, time in meetings:
            meetings_dict[time].append((x, y))
        knows_secret = [False] * n
        knows_secret[0] = True

        def get_groups(same_time_meetings: list[int]) -> list[list[int]]:
            adj_list = defaultdict(list)
            for x, y in same_time_meetings:
                adj_list[x].append(y)
                adj_list[y].append(x)

            def bfs(starting_person: int) -> set[int]:
                person_queue = deque([starting_person])
                visited_people = set([starting_person])
                while len(person_queue):
                    x = person_queue.popleft()
                    for y in adj_list[x]:
                        if y not in visited_people:
                            person_queue.append(y)
                            visited_people.add(y)
                return visited_people

            groups = []
            visited_people = set()
            for x in adj_list:
                if x not in visited_people:
                    group = bfs(x)
                    groups.append(group)
                    visited_people |= group
            return groups

        for time in sorted(meetings_dict):
            groups = get_groups(meetings_dict[time])
            for group in groups:
                for person in group:
                    if knows_secret[person]:
                        for person in group:
                            knows_secret[person] = True
                        break
        secret_knowers = []
        for i, knows in enumerate(knows_secret):
            if knows:
                secret_knowers.append(i)
        return secret_knowers
