import collections


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj_list = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = [False] * n
        connected_components = 0

        def dfs(stone: int):
            visited[stone] = True
            for neighbour_stone in adj_list[stone]:
                if not visited[neighbour_stone]:
                    dfs(neighbour_stone)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                connected_components += 1
        count = len(stones) - connected_components
        return count
