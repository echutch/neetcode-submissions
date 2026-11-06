class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = dict()

        for n in s:
            if n not in sdict:
                sdict[n] = 1
            else:
                sdict[n] += 1

        tdict = dict()

        for n in t:
            if n not in tdict:
                tdict[n] = 1
            else:
                tdict[n] += 1

        for letter in sdict:
            if letter not in tdict or sdict[letter] != tdict[letter]:
               
                return False

        return True 
        
        