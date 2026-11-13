class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_deg = set()

        for u, v in edges:
            in_deg.add(v)

        res = []
        for i in range(n):
            if i not in in_deg:
                res.append(i)

        return res
        