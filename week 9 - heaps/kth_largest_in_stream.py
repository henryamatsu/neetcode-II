class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        self.arr.append(val)
        i = len(self.arr) - 1

        while i > 0:
            p = (i - 1) // 2
        
            if self.arr[p] > self.arr[i]:
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            else:
                break

            i = p

        while len(self.arr) > self.k:
            self.pop()

        return self.arr[0]
    
    def pop(self) -> None:
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        i = 0

        while i < len(self.arr) - 1:
            l = i * 2 + 1
            r = i * 2 + 2

            smallest = i

            if l < len(self.arr) and self.arr[l] < self.arr[smallest]:
                smallest = l
            if r < len(self.arr) and  self.arr[r] < self.arr[smallest]:
                smallest = r
            
            if self.arr[smallest] == self.arr[i]:
                break

            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            
            i = smallest