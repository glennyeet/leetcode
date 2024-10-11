from heapq import heappop, heappush


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        friends = []
        available_chairs = []
        used_chairs = []
        for i in range(n):
            friends.append(i)
            available_chairs.append(i)
        friends.sort(key=lambda i: times[i][0])
        for friend in friends:
            while used_chairs and used_chairs[0][0] <= times[friend][0]:
                used_chair = heappop(used_chairs)
                heappush(available_chairs, used_chair[1])
            available_chair = heappop(available_chairs)
            if friend == targetFriend:
                return available_chair
            heappush(used_chairs, (times[friend][1], available_chair))
