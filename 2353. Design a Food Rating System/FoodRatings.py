from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class FoodRatings:
    # Hash Table + Priority Queue

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # O(nlog(n)) time, O(n) space, where n is the size of foods

        self.lookup = defaultdict(tuple)
        self.sorter = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            version = 1
            self.lookup[food] = (cuisine, rating, version)
            heappush(self.sorter[cuisine], (-rating, food, version))

    def changeRating(self, food: str, newRating: int) -> None:
        # O(1) time, O(1) space

        cuisine, _, old_version = self.lookup[food]
        new_version = old_version + 1
        self.lookup[food] = (cuisine, newRating, new_version)
        heappush(self.sorter[cuisine], (-newRating, food, new_version))

    def highestRated(self, cuisine: str) -> str:
        # O(nlog(n)) time, O(1) space

        _, food, version = self.sorter[cuisine][0]
        while version < self.lookup[food][2]:
            heappop(self.sorter[cuisine])
            _, food, version = self.sorter[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
