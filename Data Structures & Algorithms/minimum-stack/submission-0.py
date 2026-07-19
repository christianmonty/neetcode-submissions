class MinStack:

    def __init__(self):
        self.stack = []
        self.mins: float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.mins = val
        self.stack.append(val)
        self.mins = min(self.mins, val)

    def pop(self) -> None:
        self.stack.pop()
        if self.mins not in self.stack:
            self.mins = float('inf')
            for item in self.stack:
                self.mins = min(self.mins, item)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins
        
