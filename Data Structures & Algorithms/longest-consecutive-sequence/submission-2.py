class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)

        max_seq = 0
        for num in s:
            if num - 1 not in s:
                seq = 0
                while num in s:
                    num = num + 1
                    seq = seq + 1
                max_seq = max(max_seq, seq)
        return max_seq


        



                

                





    

            

        