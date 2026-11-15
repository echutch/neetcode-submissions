class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        dist = defaultdict(int)
        visited = set()

        for u, v, t in times:
            adj[u].append((v, t))

        for node in range(n):
            dist[node] = float('inf')
        dist[k] = 0
        
        min_heap = []
        heapq.heappush(min_heap, (0, k))

        time = 0
        while min_heap:
            curr_weight, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue

            visited.add(curr)
            time = curr_weight

            for next, next_weight in adj[curr]:
                if next not in visited:
                    heapq.heappush(min_heap, (curr_weight + next_weight, next))
        if len(visited) == n:
            return time
        else:
            return -1


                


        