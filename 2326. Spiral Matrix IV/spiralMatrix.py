# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_direction = 0
        x = 0
        y = 0
        m_start = 0
        n_start = 0
        m_end = m - 1
        n_end = n - 1
        dummy_node = ListNode(next=head)
        while dummy_node.next:
            matrix[x][y] = dummy_node.next.val
            if y == n_end and curr_direction % 4 == 0:  # from right to down
                curr_direction += 1
                m_start += 1
            elif x == m_end and curr_direction % 4 == 1:  # down to left
                curr_direction += 1
                n_end -= 1
            elif y == n_start and curr_direction % 4 == 2:  # left to up
                curr_direction += 1
                m_end -= 1
            elif x == m_start and curr_direction % 4 == 3:  # up to right
                curr_direction += 1
                n_start += 1
            dx, dy = directions[curr_direction % 4]
            x += dx
            y += dy
            dummy_node = dummy_node.next
        return matrix
