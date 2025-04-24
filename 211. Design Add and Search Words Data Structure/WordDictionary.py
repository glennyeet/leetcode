class Node:
    def __init__(self) -> None:
        self.edges: dict[str, Node] = {}
        self.word_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        # Trie Insert: O(n) time, O(n) space,
        # where n is the size of word

        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Node()
            cur_node = cur_node.edges[char]
        cur_node.word_end = True

    def search(self, word: str) -> bool:
        # Trie Search: O(n + 26^m) time,
        # O(1) space, where n is the
        # number of alphabetical charcters
        # in word and and m is the number of
        # wildcards(".") in word

        def dfs(word_index: int, cur_node: Node) -> bool:
            for i in range(word_index, len(word)):
                if word[i] == ".":
                    for char in cur_node.edges:
                        if dfs(i + 1, cur_node.edges[char]):
                            return True
                    return False
                elif word[i] not in cur_node.edges:
                    return False
                cur_node = cur_node.edges[word[i]]
            return cur_node.word_end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
