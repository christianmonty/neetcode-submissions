class StockSpanner:

    def __init__(self):
        # what object to initialize??
        self.stackl = []
        self.stackr = []
        

    def next(self, price: int) -> int:
        self.stackr.append(price)

        count = 1

        # what about first thing added??

        while self.stackl:
            if self.stackl[-1] <= price:
                self.stackr.append(self.stackl.pop())
                count += 1
            else:
                break

        while self.stackr:
            self.stackl.append(self.stackr.pop())
        
        return count
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)