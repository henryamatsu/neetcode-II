class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_water = 0
        while (l < r):
            l_height = heights[l]
            r_height = heights[r]
            lesser_height = min(heights[l], heights[r])

            width = r - l

            water = lesser_height * width
            max_water = max(max_water, water)

            if (l_height < r_height):
                l += 1
            else:
                r -= 1

        return max_water
