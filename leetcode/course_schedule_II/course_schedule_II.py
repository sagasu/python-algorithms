class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == [] or prerequisites[0] == []:
            return [ i for i in range(numCourses-1, -1, -1)]
        
        from collections import deque, defaultdict
        
        hs = [0] * numCourses
        course_map = defaultdict(list)
        ## construct ajacent matrix
        for after, pre in prerequisites:
            hs[after] += 1
            course_map[pre].append(after)
        rst = [i for i in range(len(hs)) if hs[i] == 0]
        q = deque(rst)
        while q:
            course = q.popleft()
            for c in course_map[course]:
                hs[c] -= 1
                if hs[c] == 0:
                    rst.append(c)
                    q.append(c)
		## check if all couses have indegree 0
        if not any(hs):
            return rst
        return []