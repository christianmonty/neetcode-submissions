class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        
        # greedy way to do this is just to have balance and counter, skip next when negative

        # how to do this with a priority queue?
        balance = 0
        counter = 0

        for t in transactions:
            if balance + t >= 0:
                balance += t
                counter += 1
        return counter