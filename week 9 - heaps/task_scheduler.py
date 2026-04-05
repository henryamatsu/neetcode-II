from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        print(counts)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        cooldown_queue = deque()
        time_elapsed = 0

        while max_heap or cooldown_queue:
            time_elapsed += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1

                if count < 0:
                    cooldown_queue.append((count, time_elapsed + n))

            if cooldown_queue and cooldown_queue[0][1] == time_elapsed:
                remaining_count = cooldown_queue.popleft()[0]
                heapq.heappush(max_heap, remaining_count)

        return time_elapsed