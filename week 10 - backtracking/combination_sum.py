from functools import reduce

class Solution:
    def get_sum(self, combination):
        return reduce(lambda x, y: x + y, combination, 0)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current_combination = []
        def traverse(index):
            if self.get_sum(current_combination) == target:
                result.append(current_combination.copy())
            elif self.get_sum(current_combination) > target:
                return

            for i in range(index, len(nums)):
                num = nums[i]
                current_combination.append(num)
                traverse(i)
                current_combination.pop()

        traverse(0)

        return result