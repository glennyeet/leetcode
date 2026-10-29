from collections import defaultdict


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        # DFS + Fenwick Tree: O((n + q) * log(n)) time, O(n * log(n)) space,
        # where q is the size of queries

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        max_log = n.bit_length()
        ancestor = [[0] * n for _ in range(max_log)]
        time_in = [0] * n
        time_out = [0] * n
        depth = [0] * n
        timer = 0

        def dfs(u: int, parent: int) -> None:
            nonlocal timer
            time_in[u] = timer
            timer += 1
            ancestor[0][u] = parent
            for v in adj_list[u]:
                if v != parent:
                    depth[v] = depth[u] + 1
                    dfs(v, u)
            time_out[u] = timer

        dfs(0, 0)
        for k in range(1, max_log):
            for u in range(n):
                ancestor[k][u] = ancestor[k - 1][ancestor[k - 1][u]]
        fenwick_tree = [0] * (n + 2)

        def xor_at(i: int, delta: int) -> int:
            i += 1
            while i < len(fenwick_tree):
                fenwick_tree[i] ^= delta
                i += i & -i

        def prefix_xor(i: int) -> int:
            res = 0
            i += 1
            while i:
                res ^= fenwick_tree[i]
                i -= i & -i
            return res

        letter_mask = [(1 << ord(char) - 97) for char in s]
        for u in range(n):
            xor_at(time_in[u], letter_mask[u])
            xor_at(time_out[u], letter_mask[u])

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            lift = depth[u] - depth[v]
            for k in range(max_log):
                if lift >> k & 1:
                    u = ancestor[k][u]
            if u == v:
                return u
            for k in reversed(range(max_log)):
                if ancestor[k][u] != ancestor[k][v]:
                    u = ancestor[k][u]
                    v = ancestor[k][v]
            return ancestor[0][u]

        answer = []
        for query in queries:
            op, *args = query.split()
            u = int(args[0])
            if op == "update":
                new_mask = 1 << (ord(args[1]) - 97)
                delta = letter_mask[u] ^ new_mask
                xor_at(time_in[u], delta)
                xor_at(time_out[u], delta)
                letter_mask[u] = new_mask
            else:
                v = int(args[1])
                a = lca(u, v)
                parity_mask = (
                    prefix_xor(time_in[u]) ^ prefix_xor(time_in[v]) ^ letter_mask[a]
                )
                answer.append(parity_mask & (parity_mask - 1) == 0)
        return answer
