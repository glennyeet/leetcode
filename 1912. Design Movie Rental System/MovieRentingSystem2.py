from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class MovieRentingSystem:
    # Hash Table + B-tree

    def __init__(self, n: int, entries: List[List[int]]):
        # O(elog(e)) time, O(e) space, where e is the size of
        # entries

        self.unrented_copies = defaultdict(SortedList)
        self.prices = {}
        for shop, movie, price in entries:
            self.unrented_copies[movie].add((price, shop))
            self.prices[shop, movie] = price
        self.rented_copies = SortedList()

    def search(self, movie: int) -> List[int]:
        # O(1) time, O(1) space

        cheapest_unrented_copies = []
        for _, shop in self.unrented_copies[movie][:5]:
            cheapest_unrented_copies.append(shop)
        return cheapest_unrented_copies

    def rent(self, shop: int, movie: int) -> None:
        # O(log(e)) time, O(1) space

        price = self.prices[shop, movie]
        self.unrented_copies[movie].remove((price, shop))
        self.rented_copies.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        # O(log(e)) time, O(1) space

        price = self.prices[shop, movie]
        self.rented_copies.remove((price, shop, movie))
        self.unrented_copies[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        # O(1) time, O(1) space

        cheapest_rented_movies = []
        for _, shop, movie in self.rented_copies[:5]:
            cheapest_rented_movies.append([shop, movie])
        return cheapest_rented_movies


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
