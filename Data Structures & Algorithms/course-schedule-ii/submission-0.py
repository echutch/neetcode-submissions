class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map_edges = defaultdict(list)

        for u, v in prerequisites:
            map_edges[u].append(v)

        cycle = set()
        visit = set()
        res = []

        def dfs_cycle(u):
            if u in cycle:
                return False
            if u in visit:
                return True
            
            cycle.add(u)
            for v in map_edges[u]:
                if dfs_cycle(v) == False:
                    return False
            cycle.remove(u)
            visit.add(u)
            res.append(u)
            return True
        
        for u in range(numCourses):
            if dfs_cycle(u) == False:
                return []
        return res

        