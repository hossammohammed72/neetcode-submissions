class Solution:
    def hammingWeight(self, n: int) -> int:
        num1s=0
        while n > 0 :
            num1s +=n%2
            n = n//2
        return num1s
        