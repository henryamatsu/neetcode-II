class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        current_subset = []

        def traverse(index):
            results.append(current_subset.copy())

            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                current_subset.append(nums[i])
                traverse(i + 1)
                current_subset.pop()

        traverse(0)

        return results