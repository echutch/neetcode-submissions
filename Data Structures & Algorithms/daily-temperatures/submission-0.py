class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        # stack: val, index
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                val, index = stack.pop()
                res[index] = i - index

            stack.append((t, i))
        return res



        