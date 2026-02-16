class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charSet = set()

        for char in s:
            charSet.add(char)
        
        for char in t:
            if char not in charSet:
                return False

        return True