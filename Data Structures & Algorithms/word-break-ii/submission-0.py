class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        idx_to_list = [[] for _ in range(len(s) + 1)] 
        idx_to_list[len(s)].append("")

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    for past_str in idx_to_list[i + len(w)]:
                        new_str = w

                        if past_str != "":
                            new_str = w + " " + past_str
                        idx_to_list[i].append(new_str)
        return idx_to_list[0]

        