class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans = []

        for i in nums:
            frequency[i] = 1 + frequency.get(i, 0)

        for i in range(k):
            max_frequency = max(list(frequency.values()))
            print(max_frequency)
            for key in frequency:
                if frequency[key] == max_frequency:
                    ans.append(key)
                    del frequency[key]
                    break

        return ans


        
        