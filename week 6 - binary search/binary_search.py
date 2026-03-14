class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1

        def traverse(start, end):
            nonlocal result

            if start > end:
                return
        
            mid = (end + start) // 2
            if target == nums[mid]:
                result = mid
            elif target < nums[mid]:
                traverse(start, mid - 1)
            else:
                traverse(mid + 1, end)

        traverse(0, len(nums) - 1)

        return result