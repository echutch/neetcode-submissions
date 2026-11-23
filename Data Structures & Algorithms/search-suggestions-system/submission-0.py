class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        pre = ""
        res = []

        products.sort()

        for c in searchWord:
            pre += c

            l, r = 0, len(products) - 1
            while l <= r:
                mid = (l + r) // 2

                if products[mid] >= pre:
                    r = mid - 1
                else:
                    l = mid + 1
            pre_list = []
            i = l
            while i < len(products) and i < l + 3 and products[i].startswith(pre):
                pre_list.append(products[i])
                i += 1
            res.append(pre_list)

        return res
            
        
