from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # Hash Table + DFS: O(n) time, O(n) space

        n = len(s)
        children = defaultdict(set)
        for i, p in enumerate(parent):
            if p != -1:
                children[p].add(i)

        def dfs1(cur_node: int, parent: int, char_last_seen: list[int]) -> None:
            last_seen = char_last_seen[ord(s[cur_node]) - ord("a")]
            if last_seen is not None:
                children[parent].remove(cur_node)
                children[last_seen].add(cur_node)
            prev_node = last_seen
            char_last_seen[ord(s[cur_node]) - ord("a")] = cur_node
            children_list = list(children[cur_node])
            for child in children_list:
                dfs1(child, cur_node, char_last_seen)
            char_last_seen[ord(s[cur_node]) - ord("a")] = prev_node

        dfs1(0, -1, [None] * 26)
        answer = [1] * n

        def dfs2(cur_node: int) -> int:
            for child in children[cur_node]:
                answer[cur_node] += dfs2(child)
            return answer[cur_node]

        dfs2(0)
        return answer
