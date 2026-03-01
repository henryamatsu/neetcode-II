class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        past_chars = set()
        longest = 0

        l = 0
        for r, r_char in enumerate(s):
            while(r_char in past_chars):
                l_char = s[l]
                past_chars.remove(l_char)
                l += 1
            
            past_chars.add(r_char)
            length = r - l + 1
            longest = max(longest, length)


        return longest