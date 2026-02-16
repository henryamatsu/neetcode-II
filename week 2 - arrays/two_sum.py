class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            num = nums[i]
            prev = hashMap.get(num)

            if prev != None:
                return sorted([i, prev])

            diff = target - num
            hashMap[diff] = i

        return []