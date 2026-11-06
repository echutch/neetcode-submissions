class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            length = len(string)
            encoded_string += str(length) + '#' + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        curr_len_str = ""
        curr_len = 0
        res = []

        while i < len(s):
            if s[i] == '#':
                curr_len = int(curr_len_str)
                curr_len_str = ""

                for j in range(i + 1, i + curr_len + 1):
                    curr_len_str += s[j]
                res.append(curr_len_str)

                curr_len_str = ""
                i += curr_len
            else:
                curr_len_str += s[i]
            i += 1
        return res

            


