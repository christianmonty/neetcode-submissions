class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # inefficient way of doing this is O(n^2) cover all substrings in str2 and ask if substring in str1 O(n^3) total
        # my gut is there is some recursive/backtracking way to try this too since if A not in str1, AB will not be in either
        # what's the math & geometry connection? Could do 1 - 26, or the ASCI #'s and do a list of those?

        # ah I missed something, must divide str1 evenly! Be a concatenation of str2!
        # could do like a "crawl" of two pointers. # well one disqualificaiton is if len(str1) % len(news) != 0
        longest = ""
        strl = strr = ""
        if len(str1) >= len(str2):
            strl = str1
            strr = str2
        else:
            strl = str2
            strr = str1

        for i in range(0, len(strl)):
            for j in range(i, len(strr)):
                news = strr[i:j+1]
                if len(news) > len(longest) and len(strl) % len(news) == 0 and len(strr) % len(news) == 0 and news in strl:
                    m, n = 0, len(news)
                    while n <= len(strl):
                        if strl[m:n] != news:
                            break
                        elif strl[m:n] == news and n == len(strl):
                            longest = news
                        m += len(news)
                        n = m + len(news)


        return longest