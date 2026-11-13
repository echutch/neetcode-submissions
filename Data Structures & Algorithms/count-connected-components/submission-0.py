class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map_edges = defaultdict(list)

        for u, v in edges:
            map_edges[u].append(v)
            map_edges[v].append(u)

        seen = set()
        queue = deque()
        count = 0

        for i in range(n):
            if i not in seen:
                count += 1
                queue.append(i)
                seen.add(i)

                while queue:
                    curr = queue.popleft()

                    for neighbor in map_edges[curr]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)

        return count

        