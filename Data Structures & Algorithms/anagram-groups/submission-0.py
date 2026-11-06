class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        output = []

        for string in strs:
            sort = ''.join(sorted(string))
            
            if sort in hashmap:
                hashmap[sort].append(string)
            else:
                hashmap[sort] = [string]

        for anagram in hashmap:
            output.append(hashmap[anagram])

        return output
        
            
        
        