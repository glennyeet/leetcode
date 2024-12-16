class Node:
    def __init__(self):
        self.edges = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.edges:
                cur.edges[char] = Node()
            cur = cur.edges[char]
        cur.word_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.edges:
                return False
            cur = cur.edges[char]
        if not cur.word_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.edges:
                return False
            cur = cur.edges[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
