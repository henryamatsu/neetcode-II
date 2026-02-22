class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result_set = set()
        result_list = []

        for i in range(len(sorted_nums)):
            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                num_i = sorted_nums[i]
                num_l = sorted_nums[l]
                num_r = sorted_nums[r]
                sum_all = num_i + num_l + num_r

                set_item = f"{num_i}, {num_l}, {num_r}"

                if sum_all == 0 and set_item not in result_set:
                    result_set.add(set_item)
                    result_list.append([num_i, num_l, num_r])
                elif sum_all < 0:
                    l += 1
                else:
                    r -= 1


        return result_list