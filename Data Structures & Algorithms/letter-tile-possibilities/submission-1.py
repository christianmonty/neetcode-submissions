class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        counts = Counter(tiles)

        def backtrack() -> int:
            count = 0

            for key in counts:
                if counts[key] > 0:
                    counts[key] -= 1

                    count += 1 + backtrack()

                    counts[key] += 1
            return count
        
        return backtrack()




        '''
        # this was my initial attempt but couldn't place in characters in the middle...
        # so had to look up solution to understand tricky "enefficient" way to do by interaitng over Counter
        # just anecdotally each tile has by itself, add to front, add to back
        # count all permutations besides duplicates

        # for each index, we can either exclude (skip), include in front, include behind, include by self
        hs = set()

        def recurse(index: i, subs: str) -> int:
            count = 0
    
            if subs != "" and subs not in hs and len(subs) <= len(tiles):
                hs.add(subs)  # make sure not to add empty string
                count += 1
            if index >= len(tiles):
                return count
            
            # 4 things to try. Must have way to retry skipped characters too
            count += recurse(index + 1, subs)
            count += recurse(index + 1, tiles[index])
            count += recurse(index + 1, subs + tiles[index])
            count += recurse(index + 1, tiles[index] + subs)
            return count
        
        return recurse(0, "")
        '''
            
