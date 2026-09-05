class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # straight hand is game of cards
        # one idea is we sort. Then put everything into a hm with val, count (from topics)
        # then start at beginning of sort, if val still in hm, take, try to take next 3 (or group size - 1) from hm
        # then take next val in sorted list, that is still present in hm
        # invariant is since consecutively increase, if start from bottom, all + 1 members of a group should be in hm

        hm = {}
        sorth = sorted(hand)

        for s in sorth:
            if s not in hm:
                hm[s] = 1
            else:
                hm[s] += 1

        if len(sorth) % groupSize != 0:
            return False

        i = 0
        while i < len(sorth): # break if hm empty
            if not hm:
                break
            if sorth[i] in hm:
                hm[sorth[i]] -= 1
                if hm[sorth[i]] == 0:
                    del hm[sorth[i]]
                end = groupSize - 1
                inc = 1
                j = sorth[i]
                while inc <= end:
                    if j + inc not in hm:
                        return False
                    else:
                        hm[j + inc] -= 1
                        if hm[j + inc] == 0:
                            del hm[j + inc]
                    inc += 1
            i += 1
        
        return True


        