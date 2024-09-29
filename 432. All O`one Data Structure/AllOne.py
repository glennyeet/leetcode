class Node:
    def __init__(self, count) -> None:
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            count = node.count + 1
            if node.next.count == count:
                next_node = node.next
            else:
                next_node = Node(count)
                next_node.prev = node
                next_node.next = node.next
                node.next.prev = next_node
                node.next = next_node
            node.keys.remove(key)
            next_node.keys.add(key)
            self.key_to_node[key] = next_node
            if not len(node.keys):
                node.prev.next = next_node
                next_node.prev = node.prev
        else:
            if self.head.next.count == 1:
                node = self.head.next
            else:
                node = Node(1)
                node.prev = self.head
                node.next = self.head.next
                self.head.next.prev = node
                self.head.next = node
            node.keys.add(key)
            self.key_to_node[key] = node

    def dec(self, key: str) -> None:
        node = self.key_to_node[key]
        count = node.count - 1
        node.keys.remove(key)
        if count >= 1:
            if node.prev.count == count:
                prev_node = node.prev
            else:
                prev_node = Node(count)
                prev_node.prev = node.prev
                prev_node.next = node
                node.prev.next = prev_node
                node.prev = prev_node
            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node
            if not len(node.keys):
                prev_node.next = node.next
                node.next.prev = prev_node
        else:
            del self.key_to_node[key]
            if not len(node.keys):
                node.prev.next = node.next
                node.next.prev = node.prev

    def getMaxKey(self) -> str:
        if self.head == self.tail.prev:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head == self.tail.prev:
            return ""
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
