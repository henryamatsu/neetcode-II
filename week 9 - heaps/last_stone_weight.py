class StoneHeap:
    def __init__(self, arr):
        self.arr = []
        for num in arr:
            self.add(num)

    def add(self, val: int):
        self.arr.append(val)
        i = len(self.arr) - 1

        while i > 0:
            p = (i - 1) // 2

            if self.arr[i] > self.arr[p]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            else:
                break

            i = p

    def pop(self) -> int:
        pop_val = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        i = 0

        while i < len(self.arr) - 1:
            l = i * 2 + 1
            r = i * 2 + 2

            largest = i

            if l < len(self.arr) and self.arr[l] > self.arr[largest]:
                largest = l
            if r < len(self.arr) and self.arr[r] > self.arr[largest]:
                largest = r

            if self.arr[i] == self.arr[largest]:
                break
            
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            i = largest

        return pop_val

    def handleCollisions(self) -> int:
        while len(self.arr) > 1:
            stone1 = self.pop()
            stone2 = self.pop()

            newStone = abs(stone1 - stone2)

            if newStone != 0:
                self.add(newStone)
        
        if len(self.arr) == 1:
            return self.arr[0]
        else:
            return 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = StoneHeap(stones)
        return heap.handleCollisions()
        