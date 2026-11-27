class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        # sort tokens, start from beg and end
        tokens.sort()

        l, r = 0, len(tokens) - 1

        score = 0
        maxscore = 0

        while l <= r:
            # edge case if l == r
            while l <= r and tokens[l] <= power:
                power -= tokens[l]
                score += 1
                maxscore = max(score, maxscore)
                l += 1
            if score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            
            if l < len(tokens) and score == 0 and power < tokens[l]:
                break
            
        return maxscore
