class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_seq = 0

        for num in s:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                max_seq = max(max_seq, length)
        return max_seq


        



                

                





    

            

        