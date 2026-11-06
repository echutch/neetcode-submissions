class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map_tasks = {}

        for task in tasks:
            map_tasks[task] = 1 + map_tasks.get(task, 0)
        
        max_heap = [(-freq, task) for (task, freq) in map_tasks.items()]
        heapq.heapify(max_heap)

        queue = deque()

        time = 0

        while max_heap or queue:
            if not max_heap:
                task, new_time = queue.popleft()
                time = new_time
            else:
                while queue and queue[0][1] <= time:
                    new_task, _ = queue.popleft()
                    heapq.heappush(max_heap, (-map_tasks[new_task], new_task))
                (neg_freq, task) = heapq.heappop(max_heap)

            map_tasks[task] -= 1
            time += 1
            if map_tasks[task] > 0:
                queue.append((task, time + n))

            
        return time

# max_heap: [(B, 1), (C, 1), (E, 1)]

# (D, 1)

# time: 9
# queue: [(D, 9)]


# A, B, C, A, B, C, D, A, B
        

        