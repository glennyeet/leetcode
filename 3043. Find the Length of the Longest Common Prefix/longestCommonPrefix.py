class Node:
    def __init__(self) -> None:
        self.edges = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def add(self, s):
        cur = self.root
        for c in s:
            if c not in cur.edges:
                cur.edges[c] = Node()
            cur = cur.edges[c]

    def search(self, s):
        cur = self.root
        count = 0
        for c in s:
            if c not in cur.edges:
                return count
            count += 1
            cur = cur.edges[c]
        return count


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = Trie()
        for num in arr1:
            prefixes.add(str(num))
        longest_prefix_len = 0
        for num in arr2:
            longest_prefix_len = max(longest_prefix_len, prefixes.search(str(num)))
        return longest_prefix_len
