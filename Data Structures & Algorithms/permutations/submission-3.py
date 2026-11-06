class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        picked = [False] * len(nums)

        def permute_recursive(nums, perm, picked):
            if len(perm) == len(nums):
                self.res.append(perm)
                return

            for i in range(len(nums)):
                if not picked[i]:
                    picked_path = picked.copy()
                    picked_path[i] = True
                    perm_path = perm.copy()
                    perm_path.append(nums[i])
                    permute_recursive(nums, perm_path, picked_path)
        
        permute_recursive(nums, [], picked)
        return self.res

        # nums: [1, 2, 3]
        # perm: [1]
        # picked: [T, F, F]
        # res: []




        