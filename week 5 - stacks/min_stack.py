class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = val if len(self.min_stack) == 0 else min(self.getMin(), val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        top_index = len(self.stack) - 1
        return self.stack[top_index]     

    def getMin(self) -> int:
        top_index = len(self.min_stack) - 1
        return self.min_stack[top_index]
