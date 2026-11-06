class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphMap = {i: [] for i in range(n)}
        for edge in edges:
            first, second = edge
            graphMap[first].append(second)
            graphMap[second].append(first)

        visited = set()
        stack = []
        stack.append((0, -1))

        while stack:
            curr, parent = stack.pop()
            if curr in visited:
                return False
            else:
                visited.add(curr)

            for neighbor in graphMap[curr]:
                if parent != neighbor:
                    stack.append((neighbor, curr))
        return len(visited) == n
            
        
        