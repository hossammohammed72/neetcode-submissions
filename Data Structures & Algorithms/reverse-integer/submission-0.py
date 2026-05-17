class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        while x != 0:
            mod = 10 if x > 0 else -10
            print(x)
            y += x%mod
            y *=10
            if x > 0 : 
                x = x // 10 
            else: 
                x = int(x/10)
        if y > 2**31 -1 or y < -2**31:
            return 0 
        return y//10

        