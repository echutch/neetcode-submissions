class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map_edges = defaultdict(list)
        for u, v in prerequisites:
            map_edges[u].append(v)

        visited = set()

        def dfs_cycle(u):
            if u in visited:
                return False
            
            if map_edges[u] == []:
                return True

            visited.add(u)
            for v in map_edges[u]:
                if not dfs_cycle(v):
                    return False
            visited.remove(u)
            return True
        
        for u in range(numCourses):
            if not dfs_cycle(u):
                return False
        
        return True

