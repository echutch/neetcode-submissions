class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        out = []

        if k > 0:
            for i, num in enumerate(code):
                res = 0
                for j in range(k):
                    res += code[(i + j + 1) % n]
                out.append(res)
        elif k < 0:
            for i, num in enumerate(code):
                res = 0
                for j in range(-k):
                    res += code[(i - j - 1) % n]
                out.append(res)
        else:
            return [0] * len(code)

        return out
