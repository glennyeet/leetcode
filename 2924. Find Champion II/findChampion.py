class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inverted_adj_list = [[] for _ in range(n)]
        for src_node, dest_node in edges:
            inverted_adj_list[dest_node].append(src_node)
        champions = []
        for node, neighbours in enumerate(inverted_adj_list):
            if len(neighbours) == 0:
                champions.append(node)
        if len(champions) == 1:
            return champions[0]
        return -1
