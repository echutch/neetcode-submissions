class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def make_comb(i, combo):
            if i > n: 
                if k == len(combo):
                    res.append(combo.copy())
                return

            combo.append(i)
            make_comb(i + 1, combo)
            combo.pop()
            make_comb(i + 1, combo)

        make_comb(1, [])
        return res

        


        