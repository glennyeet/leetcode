from typing import List
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right


class Router:
    # Hash Table + Queue + Binary Search

    def __init__(self, memoryLimit: int):
        # O(1) time, O(1) space

        self.memory_limit = memoryLimit
        self.packets = set()
        self.packet_queue = deque()
        self.destination_to_timestamps = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # O(n) time, O(1) space, where n is the size of packets_queue

        if (source, destination, timestamp) in self.packets:
            return False
        if len(self.packet_queue) == self.memory_limit:
            deleted_source, deleted_destination, deleted_timestamp = (
                self.packet_queue.popleft()
            )
            self.packets.remove(
                (deleted_source, deleted_destination, deleted_timestamp)
            )
            self.destination_to_timestamps[deleted_destination].popleft()
        self.packets.add((source, destination, timestamp))
        self.packet_queue.append((source, destination, timestamp))
        self.destination_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        # O(n) time, O(1) space

        if not self.packet_queue:
            return []
        source, destination, timestamp = self.packet_queue.popleft()
        self.packets.remove((source, destination, timestamp))
        self.destination_to_timestamps[destination].popleft()
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # O(log(n)) time, O(1) space

        return bisect_right(
            self.destination_to_timestamps[destination], endTime
        ) - bisect_left(self.destination_to_timestamps[destination], startTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
