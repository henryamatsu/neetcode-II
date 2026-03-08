class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []

        for i, start in enumerate(position):
            time = (target - start) / speed[i]

            times.append([start, time])

        sorted_times = sorted(times)
        print(sorted_times)

        fleet_count = 0
        slowest = 0
        for car in reversed(sorted_times):
            if car[1] > slowest:
                slowest = car[1]
                fleet_count += 1

        return fleet_count
            