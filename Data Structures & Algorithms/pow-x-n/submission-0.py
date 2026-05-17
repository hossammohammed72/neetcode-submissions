class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        power = abs(n)
        for i in range(power):
            res*=x
        if n < 0:
            return 1/res
        
        return res
        