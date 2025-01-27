from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # DFS: O(c(c + p) + q) => O(c^3 + q) time, O(c + p) => O(c^2) space, where
        # c is the number of courses, p is the number of prerequisites, and q is
        # the number of queries

        inverted_graph = defaultdict(list)
        for a, b in prerequisites:
            inverted_graph[b].append(a)
        prerequisite_lookup = defaultdict(set)

        def find_prerequisites(cur_node: int) -> int:
            if cur_node not in prerequisite_lookup:
                for prerequisite in inverted_graph[cur_node]:
                    prerequisite_lookup[cur_node] |= find_prerequisites(prerequisite)
                prerequisite_lookup[cur_node].add(cur_node)
            return prerequisite_lookup[cur_node]

        for course in range(numCourses):
            find_prerequisites(course)
        answer = []
        for u, v in queries:
            answer.append(u in prerequisite_lookup[v])
        return answer
