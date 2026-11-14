class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        for i, c in enumerate(strs[0]):
            for st in strs:
                if i >= len(st) or st[i] != c:
                    return common
            common += c
        return common
        