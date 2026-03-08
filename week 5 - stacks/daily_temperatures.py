class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result[i] is count of days after temperatures[i] until warmer day is found
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if i > 0:
                top_temp = stack[len(stack) - 1][0]
                while len(stack) > 0 and temp > top_temp:
                    top = stack.pop()
                    days_passed = i - top[1]
                    result[top[1]] = days_passed

                    if len(stack) > 0:
                        top_temp = stack[len(stack) - 1][0]

            stack.append([temp, i])

        return result