class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate_helper(n_open, n_closed, curr):
            if n_open == 0 and n_closed == 0:
                res.append(curr)
            elif n_open == 0:
                generate_helper(n_open, n_closed - 1, curr + ")")
            elif n_closed == 0 or n_open == n_closed:
                generate_helper(n_open - 1, n_closed, curr + "(")
            else:
                generate_helper(n_open - 1, n_closed, curr + "(")
                generate_helper(n_open, n_closed - 1, curr + ")")
        
        generate_helper(n, n, "")
        return res



        