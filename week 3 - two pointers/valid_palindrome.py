class Solution:
    import re

    def isPalindrome(self, s: str) -> bool:
        subbed = re.sub(r"\W", "", s).lower()

        for l,r in zip(subbed, reversed(subbed)):
            if l != r:
                return False

        return True