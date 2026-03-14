class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_index = -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            l_num = nums[l]
            r_num = nums[r]
            m_num = nums[m]

            if m_num == target:
                target_index = m
                break

            elif l_num <= m_num:
                if l_num <= target < m_num:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if m_num < target <= r_num:
                    l = m + 1
                else:
                    r = m - 1

        return target_index