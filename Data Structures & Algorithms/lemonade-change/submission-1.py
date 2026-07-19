class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        # apparently we need to greedily return 10's (preserve 5's) then 5's
        # 3 cases: given a 5, no change. given a 10, must return a 5. given a 20, first try to return 10+5, else 3 5's
        # notice that being given twenties does nothing for us!

        fives = 0
        tens = 0
        twens = 0

        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                if not fives:
                    return False
                else:
                    fives -= 1
                    tens += 1
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                    twens += 1
                elif fives >= 3:
                    fives -= 3
                    twens += 1
                else:
                    return False
            
        return True


        '''
        # as far as I see it we need to track bank account, and iterate over each customer
        # 3 change amounts are: 0 (if 5), 5 (if 10), and 15 (if 20)
        # Given 5: we're good, no change
        # Given 10: we need at least one 5 to give back
        # Given 20: we can give back 3 fives, OR 1 10 and 1 five, that's it. But issue is which should we??
        # issue: if we have to explore two paths, not efficient solution
        # issue with balance idea is does $20 balance mean four 5's, 2 10's, or a $20? Or two 5's and 1 ten

        # Recall: Greedy means local optimal is global optimal
        # maybe try removing $5 from each? to see amount of change needed
        # then compare previously balance with amount of change needed at each i as a greedy method?
        # ALWAYS TRY TO TRANSFORM THE PROBLEM

        change = [0] * len(bills)
        for idx, b in enumerate(bills):
            change[idx] = bills[idx] - 5

        balance = 0
        for idx, b in enumerate(bills):
            if change[idx] > 0:
                if balance < change[idx]:
                    return False
                balance -= change[idx]
            balance += b
        
        return True
        '''
