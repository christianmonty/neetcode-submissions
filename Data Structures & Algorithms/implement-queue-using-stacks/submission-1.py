from collections import deque

class MyQueue:

    def __init__(self):
        self.l = deque()
        self.r = deque()
        

    def push(self, x: int) -> None:
        self.l.append(x)
        # put on left stack
        

    def pop(self) -> int:
        # pop all from left stack into right stack
        # then pop once from right queue
        # then put all back

        if self.r:
            return self.r.pop()
        
        # trick is only need to spill over when self.r runs out
        while self.l:
            self.r.append(self.l.pop())
        return self.r.pop()

    def peek(self) -> int:
        if self.r:
            return self.r[-1]
        elif self.l:
            return self.l[0]
        else:
            return -1

    def empty(self) -> bool:
        if self.l or self.r:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()