class Solution:
    def isHappy(self, n: int) -> bool:
        saved = set()
        while True:
            print(n)
            if n == 1:
                return True

            digits = str(n)
            new_n = 0
            for d in digits:
                new_n += int(d)**2
            n = new_n
            if n in saved:
                return False
            else:
                saved.add(n)
        
        