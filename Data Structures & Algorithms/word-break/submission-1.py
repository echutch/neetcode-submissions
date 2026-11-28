class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # break(i): true if s[i:] can be broken into words in wordDict
        # break(len(s)) = True

        wbreak = [False] * (len(s) + 1)
        wbreak[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s)) and s[i : i + len(word)] == word:
                    wbreak[i] = wbreak[i + len(word)]
                if wbreak[i]:
                    break
        print(wbreak)
        return wbreak[0]
        