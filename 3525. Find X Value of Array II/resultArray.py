from typing import List


class Solution:
    class SegmentTree:
        def __init__(self, n: int, k: int, arr: list[int]) -> None:
            self.prefix_histogram = [[0] * k for _ in range(4 * n)]
            self.segment_product = [None] * (n * 4)
            self.n = n
            self.k = k
            self.build(0, 0, n - 1, arr)

        def merge(self, node: int) -> None:
            self.prefix_histogram[node] = [0] * self.k
            left = node * 2 + 1
            right = node * 2 + 2
            for i in range(self.k):
                self.prefix_histogram[node][i] += self.prefix_histogram[left][i]
            for i in range(self.k):
                self.prefix_histogram[node][
                    (self.segment_product[left] * i) % self.k
                ] += self.prefix_histogram[right][i]
            self.segment_product[node] = (
                self.segment_product[left] * self.segment_product[right]
            ) % self.k

        def build(self, node: int, left: int, right: int, arr: list[int]) -> None:
            if left == right:
                self.prefix_histogram[node] = [0] * self.k
                v = arr[left]
                self.prefix_histogram[node][v % self.k] += 1
                self.segment_product[node] = v % self.k
                return
            mid = (left + right) // 2
            self.build(node * 2 + 1, left, mid, arr)
            self.build(node * 2 + 2, mid + 1, right, arr)
            self.merge(node)

        def update(self, node: int, left: int, right: int, i: int, v: int) -> None:
            if left == right:
                self.prefix_histogram[node] = [0] * self.k
                self.prefix_histogram[node][v % self.k] += 1
                self.segment_product[node] = v % self.k
                return
            mid = (left + right) // 2
            if i <= mid:
                self.update(node * 2 + 1, left, mid, i, v)
            else:
                self.update(node * 2 + 2, mid + 1, right, i, v)
            self.merge(node)

        def query(self, node: int, left: int, right: int, i: int):
            if left == right:
                prefix_histogram = self.prefix_histogram[node][:]
                segment_product = self.segment_product[node]
                return [prefix_histogram, segment_product]
            mid = (left + right) // 2
            if i <= mid:
                left_res = self.query(node * 2 + 1, left, mid, i)
                right_i = node * 2 + 2
                right_res = [
                    self.prefix_histogram[right_i],
                    self.segment_product[right_i],
                ]
                merged_product = (left_res[1] * right_res[1]) % self.k
                merged_histogram = left_res[0][:]
                for i in range(self.k):
                    merged_histogram[(left_res[1] * i) % self.k] += right_res[0][i]
                return [merged_histogram, merged_product]
            else:
                return self.query(node * 2 + 2, mid + 1, right, i)

    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        # Segment Tree + Math: O((n + q) * k * log(n)) time, O(n * k) space, where
        # q is the size of queries

        n = len(nums)
        segment_tree = self.SegmentTree(n, k, nums)
        ans = []
        for index, value, start, x in queries:
            segment_tree.update(0, 0, n - 1, index, value)
            query_res = segment_tree.query(0, 0, n - 1, start)
            ans.append(query_res[0][x])
        return ans
