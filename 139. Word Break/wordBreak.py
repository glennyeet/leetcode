from typing import List
from functools import cache


class Node:
    def __init__(self) -> None:
        self.edges = {}
        self.word_end = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Node()
            cur_node = cur_node.edges[char]
        cur_node.word_end = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                return False
            cur_node = cur_node.edges[char]
        return cur_node.word_end


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie + Top-down DP: O(d * w + n^2) time, O(n * w)
        # space, where d is the size of wordDict and w is the size
        # of a word in wordDict

        n = len(s)
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        @cache
        def dp(start_index: int) -> bool:
            if start_index == n:
                return True
            for end_index in range(start_index, n):
                if trie.search(s[start_index : end_index + 1]) and dp(end_index + 1):
                    return True
            return False

        return dp(0)
