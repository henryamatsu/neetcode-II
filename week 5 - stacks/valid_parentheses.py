class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = dict({
            "{": "}",
            "[": "]",
            "(": ")"
        })

        stack = []
        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                latest = stack.pop()
                if bracket_map[latest] != char:
                    return False
            
        if len(stack) == 0:
            return True

        return False