from typing import List


class Node:
    def __init__(self) -> None:
        self.edges: dict[str, Node] = {}
        self.min_container_index = None


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def search(self, query: str) -> int:
        cur = self.root
        cur_min_container_index = cur.min_container_index
        for char in query:
            if char in cur.edges:
                cur = cur.edges[char]
                cur_min_container_index = cur.min_container_index
            else:
                return cur_min_container_index
        return cur_min_container_index

    def process(self, word: str, index: int) -> None:
        cur = self.root
        cur.min_container_index = index
        for char in word:
            if char not in cur.edges:
                cur.edges[char] = Node()
            cur = cur.edges[char]
            cur.min_container_index = index


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        # Trie: O(c * log(c)) time, O(c) space, where c is the size of
        # wordsContainer

        reversed_words = []
        for i, word in enumerate(wordsContainer):
            reversed_words.append((word[::-1], i))
        reversed_words.sort(key=lambda w: (len(w[0]), w[1]), reverse=True)
        trie = Trie()
        for word, i in reversed_words:
            trie.process(word, i)
        ans = []
        for query in wordsQuery:
            ans.append(trie.search(query[::-1]))
        return ans
