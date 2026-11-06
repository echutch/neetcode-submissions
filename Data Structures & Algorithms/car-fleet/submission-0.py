class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p in pair:
            time = (target - p[0]) / p[1]

            if stack and time <= stack[-1][0]:
                stack[-1].append(time)
            else:
                stack.append([time])
        return len(stack)





        