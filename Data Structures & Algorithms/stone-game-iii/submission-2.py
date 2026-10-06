class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        totalScore = sum(stoneValue)

        # trick here is that Bob's stones shouldn't count towards Alice's total...
        dp = [0] * (len(stoneValue) + 3)


        def recurse(index: int, alice: bool) -> int:
            # key is if not alice, still want to play optimally, but only want to set dp score when alice?
            # or do we if alice choose max, if bob choose min? Does that make sense? Bob wants min for Alice?
            if index >= len(stoneValue):
                return 0
            if alice and dp[index]:
                return dp[index]
            justone = stoneValue[index]
            call1 = recurse(index + 1, not alice)
            justtwo = sum(stoneValue[index:index+2])
            call2 = recurse(index + 2, not alice)
            allthree = sum(stoneValue[index:index+3])
            call3 = recurse(index + 3, not alice)
            if alice:
                dp[index] = max(justone + call1, justtwo + call2, allthree + call3) # just dp Alice's advantagge
            return max(justone + call1, justtwo + call2, allthree + call3) if alice else min(call1, call2, call3)

        aliceScore = recurse(0, True)
        bobScore = totalScore - aliceScore

        if aliceScore == bobScore:
            return "Tie"
        return "Alice" if aliceScore > bobScore else "Bob"