"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# correct solution: like my initial intuition, check if all the values of current grid are identical BEFORE recursing...

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # first attempt, will try not to overcomplicate it
        # note this attempt will create Nodes for all the leaves if same #

        # this is the part to think more about as it's making too many nodes

        # my original solution below was correct, I just flipped tr and bl per this format
        # other optimizations are deleting wasted nodes (duplicate or duplicates) or iterating first
        
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        newsize = len(grid) // 2 # int division

        tl = self.construct([row[:newsize] for row in grid[:newsize]])
        tr = self.construct([row[newsize:] for row in grid[:newsize]])
        bl = self.construct([row[:newsize] for row in grid[newsize:]])
        br = self.construct([row[newsize:] for row in grid[newsize:]])

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
            if tl.val and tr.val and bl.val and br.val or not (tl.val or tr.val or bl.val or br.val):
                return Node(tl.val, True, None, None, None, None)
        
        return Node(False, False, tl, tr, bl, br)

    


        # what's wrong with my solution:
        # 1. Too many nulls
        # 2. Right order of the trees, must have messed up tl, tr etc.

        # if we get to only four blocks total (2 x 2)
        # make four leafs if needed (dif), otherwise make leaf and set val to val
        # and recurse
        # if single value, return isLeaf = True and set the value
        # Then have parent decide that if all 4 leafs return same value, we return that we are a leaf, and then value
        # if entire grid returns that, then we only make a single node
        # if something returns not a leaf, made that a regular node

        # one thing I'm confused by is if we recurse down to a single square, how we elevate up that it's all the same value vs. being mixed value
        # basically we don't need a ton of extra leaves, so best to not waste space
        