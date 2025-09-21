from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class MovieRentingSystem:
    # Hash Table + Priority Queue

    def __init__(self, n: int, entries: List[List[int]]):
        # O(elog(e)) time, O(e) space, where e is the size of
        # entries

        self.prices = {}
        self.unrented_copies = defaultdict(list)
        for shop, movie, price in entries:
            self.prices[shop, movie] = price
            heappush(self.unrented_copies[movie], (price, shop))
        self.rented_copies = set()
        self.sorted_rented_copies = []

    def search(self, movie: int) -> List[int]:
        # O(elog(e)) time, O(e) space

        cheapest_unrented_copies = []
        cheapest_shops = []
        while self.unrented_copies[movie] and len(cheapest_shops) < 5:
            price, shop = heappop(self.unrented_copies[movie])
            cheapest_unrented_copies.append((price, shop))
            if (shop, movie) in self.rented_copies:
                continue
            cheapest_shops.append(shop)
        for price, shop in cheapest_unrented_copies:
            heappush(self.unrented_copies[movie], (price, shop))
        return cheapest_shops

    def rent(self, shop: int, movie: int) -> None:
        # O(elog(e)) time, O(1) space

        self.rented_copies.add((shop, movie))
        heappush(self.sorted_rented_copies, (self.prices[shop, movie], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        # O(e) time, O(1) space

        self.rented_copies.remove((shop, movie))

    def report(self) -> List[List[int]]:
        # O(elog(e)) time, O(e) space

        cheapest_rented_copies = []
        cheapest_rented_movies = []
        while self.sorted_rented_copies and len(cheapest_rented_movies) < 5:
            price, shop, movie = heappop(self.sorted_rented_copies)
            cheapest_rented_copies.append((price, shop, movie))
            if (shop, movie) not in self.rented_copies or (
                cheapest_rented_movies and cheapest_rented_movies[-1] == [shop, movie]
            ):
                continue
            cheapest_rented_movies.append([shop, movie])
        for price, shop, movie in cheapest_rented_copies:
            heappush(self.sorted_rented_copies, (price, shop, movie))
        return cheapest_rented_movies


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
