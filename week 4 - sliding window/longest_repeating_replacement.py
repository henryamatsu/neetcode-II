from functools import reduce

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        past_chars = dict()
        longest = 0
        for r,r_char in enumerate(s):
            if r_char not in past_chars:
                past_chars[r_char] = 0
            
            past_chars[r_char] += 1
        
            vals = list(past_chars.values())
            map_size = reduce(lambda x,y: x+y, vals)
            mode_count = max(vals)
            non_mode_count = map_size - mode_count
            
            if non_mode_count > k:
                l_char = s[l]
                l += 1
                past_chars[l_char] -= 1

            length = r - l + 1
            longest = max(longest, length)

        return longest
            
