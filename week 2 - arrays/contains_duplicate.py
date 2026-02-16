class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pastNums = set()

        for num in nums:
            if num in pastNums:
                return True
            
            pastNums.add(num)
        
        return False