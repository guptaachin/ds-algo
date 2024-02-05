
class MinStack:
    def __init__(self):
        self.stack = [] # list of tuples

    def push(self, val: int) -> None:
        min_ = None
        if len(self.stack) > 0:
            top = self.stack[-1]
            min_ = min(top[-1], val)
        else: # first element
            min_ = val
        self.stack.append((val, min_))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
