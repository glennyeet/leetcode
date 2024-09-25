class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.edges = {}


class Trie:
    def __init__(self) -> None:
        self.root = Node(0)

    def add(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.edges:
                cur.edges[c] = Node(1)
            else:
                cur.edges[c].val += 1
            cur = cur.edges[c]

    def search(self, word: str):
        cur = self.root
        score = 0
        for c in word:
            if c not in cur.edges:
                return score
            cur = cur.edges[c]
            score += cur.val
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        answer = []
        for word in words:
            answer.append(trie.search(word))
        return answer
