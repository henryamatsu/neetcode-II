class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current_subset = []
        candidates.sort()

        def traverse(index):
            if sum(current_subset) == target:
                result.append(current_subset.copy())
            elif sum(current_subset) > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                current_subset.append(num)
                traverse(i + 1)
                current_subset.pop()
        
        traverse(0)

        return result