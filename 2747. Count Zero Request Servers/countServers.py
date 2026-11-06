from collections import Counter
from typing import List


class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        # Hash Table + Sliding Window: O(l * log(l) + q * log(q)) time,
        # O(n + l + q) space

        l = len(logs)
        q = len(queries)
        sorted_logs = sorted(logs, key=lambda l: l[1])
        received_requests = Counter()
        arr = [0] * q
        i = 0
        j = 0
        sorted_old_indices = sorted(range(q), key=lambda k: queries[k])
        for k in sorted_old_indices:
            query = queries[k]
            while j < l and sorted_logs[j][1] <= query:
                server_id = sorted_logs[j][0]
                received_requests[server_id] += 1
                j += 1
            while i < j and sorted_logs[i][1] < query - x:
                server_id = sorted_logs[i][0]
                received_requests[server_id] -= 1
                if received_requests[server_id] == 0:
                    del received_requests[server_id]
                i += 1
            arr[k] = n - len(received_requests)
        return arr
