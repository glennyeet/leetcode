from typing import List


class Node:
    def __init__(self) -> None:
        self.edges: dict[str, Node] = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Node()
            cur_node.edges[char].count += 1
            cur_node = cur_node.edges[char]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Trie: O(m * n) time, O(c) space, where m is the
        # length of a string in strs and c is the number
        # of unique characters per slot (size of the trie)

        n = len(strs)
        trie = Trie()
        for str in strs:
            trie.insert(str)
        longest_common_prefix = []
        cur_node = trie.root
        for char in strs[0]:
            if cur_node.edges[char].count != n:
                break
            longest_common_prefix.append(char)
            cur_node = cur_node.edges[char]
        return "".join(longest_common_prefix)
