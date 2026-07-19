class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = [set() for __ in range(numCourses)] # check syntax

        for pair in prerequisites:
            courses[pair[0]].add(pair[1])
            for vals in courses[pair[1]]:
                if vals not in courses[pair[0]]:
                    courses[pair[0]].add(vals)
        
        for index, c in enumerate(courses):
            for item in c:
                if index in courses[item]:
                    return False

        return True