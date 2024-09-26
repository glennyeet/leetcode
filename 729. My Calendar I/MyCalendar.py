class BSTNode:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = BSTNode(start, end)
            return True
        cur = self.root
        prev = None
        left = None
        while cur is not None:
            if end <= cur.start:
                prev = cur
                cur = cur.left
                left = True
            elif start >= cur.end:
                prev = cur
                cur = cur.right
                left = False
            else:
                return False
        if left:
            prev.left = BSTNode(start, end)
        else:
            prev.right = BSTNode(start, end)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
