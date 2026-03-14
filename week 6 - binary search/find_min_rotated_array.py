import math

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        smallest = math.inf
        while l <= r:
            m = (l + r) // 2

            l_num = nums[l]
            r_num = nums[r]
            m_num = nums[m]

            smallest = min(smallest, m_num)

            if m_num < r_num:
                r = m - 1
            else:
                l = m + 1

        return smallest