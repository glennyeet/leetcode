from typing import List


class Node:
    def __init__(self) -> None:
        self.next_letters: dict[str, Node] = {}
        self.root_word = None


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, root: str) -> None:
        cur_node = self.root
        for char in root:
            if char not in cur_node.next_letters:
                cur_node.next_letters[char] = Node()
            cur_node = cur_node.next_letters[char]
        cur_node.root_word = root

    def find_smallest_root(self, word: str) -> str:
        cur_node = self.root
        for char in word:
            if char not in cur_node.next_letters:
                break
            cur_node = cur_node.next_letters[char]
            if cur_node.root_word:
                return cur_node.root_word
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Trie: O(d * w + s * w) time, O(d * w + s * w) space, where d is the size of
        # dictionary, w is the average length of each word, and s is the number of
        # words in sentence

        roots_trie = Trie()
        for root in dictionary:
            roots_trie.insert(root)
        sentence_words = sentence.split(" ")
        new_sentence = []
        for word in sentence_words:
            new_sentence.append(roots_trie.find_smallest_root(word))
        return " ".join(new_sentence)
