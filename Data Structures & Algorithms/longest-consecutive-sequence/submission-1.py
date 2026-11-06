class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)


        longest_seq = []
        for num in s:
            if num - 1 not in s:
                seq = []
                while num in s:
                    seq.append(num)
                    print(num)
                    num = num + 1

                if len(seq) > len(longest_seq):
                    longest_seq = seq

        return len(longest_seq)


    

            

        