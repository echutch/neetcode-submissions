class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        sub = set()

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            length = max(length, r - l + 1)
      

        return length
            


        