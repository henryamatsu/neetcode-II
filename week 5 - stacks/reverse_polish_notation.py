import math

class Solution:
    def doMath(self, num1, num2, operator) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return math.trunc(num1 / num2)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"

        stack = []

        for char in tokens:
            if char not in operators:
                num = int(char)
                stack.append(num)
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                result = self.doMath(num1, num2, char)
                stack.append(result)

        return stack[0]