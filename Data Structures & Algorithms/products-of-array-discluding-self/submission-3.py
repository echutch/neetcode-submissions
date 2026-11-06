class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        skip_product = 1
        test_zero = 0
        for num in nums:
            total_product *= num
            if num != 0:
                skip_product *= num
            else:
                test_zero += 1

        res = []

        for num in nums:
            if num == 0 and test_zero == 1:
                res.append(skip_product)
            elif num == 0:
                res.append(0)
            else:
                res.append(int(total_product / num))

        return res


            
        