from typing import List


class Node:
    def __init__(self) -> None:
        self.children = [None, None]
        self.number = None


class Trie:
    def __init__(self, n: int) -> None:
        self.root = Node()
        self.n = n

    def insert(self, number: int) -> None:
        cur_node = self.root
        for offset in reversed(range(self.n)):
            bit = int(number & 1 << offset > 0)
            if not cur_node.children[bit]:
                cur_node.children[bit] = Node()
            cur_node = cur_node.children[bit]
        cur_node.number = number

    def find_max_xor(self, number: int) -> int:
        cur_node = self.root
        for offset in reversed(range(self.n)):
            bit = 1 - (number & 1 << offset > 0)
            if cur_node.children[bit]:
                cur_node = cur_node.children[bit]
            else:
                cur_node = cur_node.children[1 - bit]
        return number ^ cur_node.number


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Trie: O(nlog(m)) time, O(nlog(m)) space, where
        # n is the size of nums and m is the largest number in nums

        trie = Trie(len(bin(max(nums))))
        for num in nums:
            trie.insert(num)
        max_xor = 0
        for num in nums:
            max_xor = max(max_xor, trie.find_max_xor(num))
        return max_xor
