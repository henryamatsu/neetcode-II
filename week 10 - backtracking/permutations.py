class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []

        def traverse(remaining_set):
            if len(remaining_set) == 0:
                result.append(current_subset.copy())
                return

            for num in remaining_set:
                current_subset.append(num)
                traverse([n for n in remaining_set if n != num])
                current_subset.pop()            


        traverse(nums)
        return result