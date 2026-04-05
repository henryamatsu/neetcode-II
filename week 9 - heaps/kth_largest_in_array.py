class MinHeap:
    def __init__(self, nums, k):
        self.arr = []
        self.k = k

        for num in nums:
            self.add(num)
    
    def add(self, num):
        self.arr.append(num)
        i = len(self.arr) - 1

        while i > 0:
            p = (i - 1) // 2

            if self.arr[i] < self.arr[p]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            else:
                break
            
            i = p

        while len(self.arr) > self.k:
            self.remove()
    
    def remove(self):
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        i = 0

        while i < len(self.arr):
            l = i * 2 + 1
            r = i * 2 + 2

            smallest = i
            if l < len(self.arr) and self.arr[l] < self.arr[smallest]:
                smallest = l
            if r < len(self.arr) and self.arr[r] < self.arr[smallest]:
                smallest = r
            
            if smallest == i:
                break

            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]

            i = smallest
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap(nums, k)

        return heap.arr[0]    