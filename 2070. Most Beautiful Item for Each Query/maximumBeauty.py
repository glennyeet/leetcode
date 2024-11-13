from bisect import bisect_right


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        sorted_items = items.copy()
        sorted_items.sort()
        max_beauties = []
        max_beauty = 0
        for item in sorted_items:
            max_beauty = max(max_beauty, item[1])
            if max_beauties and max_beauties[-1][0] == item[0]:
                max_beauties[-1][1] = max_beauty
            else:
                max_beauties.append([item[0], max_beauty])

        # def binary_search(target: int) -> int:
        #     low = 0
        #     high = len(max_beauties) - 1
        #     while low <= high:
        #         mid = low + (high - low) // 2
        #         if max_beauties[mid][0] <= target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
        #     return low

        answer = []
        for query in queries:
            # index = binary_search(query)
            index = bisect_right(max_beauties, [query, 10**9])
            if index == 0:
                answer.append(0)
            else:
                answer.append(max_beauties[index - 1][1])
        return answer
