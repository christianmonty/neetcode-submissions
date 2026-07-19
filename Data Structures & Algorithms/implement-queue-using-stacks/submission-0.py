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
        while self.l:
            self.r.append(self.l.pop())
        retval = self.r.pop()

        while self.r:
            self.l.append(self.r.pop())
        return retval
        

    def peek(self) -> int:
        return self.l[0]

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