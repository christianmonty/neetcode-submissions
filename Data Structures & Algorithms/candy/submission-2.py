class Solution:
    def candy(self, ratings: List[int]) -> int:
        # try again, just try brute force first
        candies = [1 for _ in ratings]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i - 1] + 1
            j = i - 1
            if ratings[i] < ratings[j] and candies[i] == candies[j]:
                while j >= 0:
                    if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                        candies[j] = candies[j + 1] + 1
                    j -= 1

        return sum(candies)