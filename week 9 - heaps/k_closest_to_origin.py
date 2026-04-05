import math
import heapq
class Solution:
    def euc_calc(self, point):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = [(-(self.euc_calc(point)), point) for point in points]
        heapq.heapify(max_heap)

        for _ in range(len(max_heap) - k):
            heapq.heappop(max_heap)
        
        print(max_heap)

        return [entry[1] for entry in max_heap]