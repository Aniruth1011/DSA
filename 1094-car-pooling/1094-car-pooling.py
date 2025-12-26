class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []  # min-heap: [end_location, num_passengers]
        current_passengers = 0

        for num_passengers, start, end in trips:
            # Drop off passengers whose trips have ended
            while heap and heap[0][0] <= start:
                drop_end, drop_num = heapq.heappop(heap)
                current_passengers -= drop_num

            # Pick up new passengers
            heapq.heappush(heap, [end, num_passengers])
            current_passengers += num_passengers

            # Check if capacity exceeded
            if current_passengers > capacity:
                return False

        return True
