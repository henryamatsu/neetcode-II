class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current_subset = []

        def traverse(index):
            result.append(current_subset.copy())
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                current_subset.append(nums[i])
                traverse(i + 1)
                current_subset.pop()
        
        traverse(0)
        return result