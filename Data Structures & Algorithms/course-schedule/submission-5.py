class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_prereq = defaultdict(list)
        indeg = [0] * numCourses

        for course, pre in prerequisites:
            map_prereq[pre].append(course)
            indeg[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)

        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for next in map_prereq[curr]:
                indeg[next] -= 1

                if indeg[next] == 0:
                    queue.append(next)

        print(order)
        return len(order) == numCourses

        



        