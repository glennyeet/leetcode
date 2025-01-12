# Trie: O(nm) time, O(nm) space, where n is the number
# of words and m is the length of the longest word


class Node:
    def __init__(self) -> None:
        self.edges = {}
        self.prefix_suffixes = 0


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char1, char2 in zip(word, reversed(word)):
            if (char1, char2) not in cur.edges:
                cur.edges[(char1, char2)] = Node()
            cur = cur.edges[(char1, char2)]
            cur.prefix_suffixes += 1

    def count_prefix_suffixes(self, word: str) -> bool:
        cur = self.root
        for char1, char2 in zip(word, reversed(word)):
            if (char1, char2) not in cur.edges:
                return 0
            cur = cur.edges[(char1, char2)]
        return cur.prefix_suffixes


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        index_pairs = 0
        trie = Trie()
        for word in reversed(words):
            index_pairs += trie.count_prefix_suffixes(word)
            trie.insert(word)
        return index_pairs
