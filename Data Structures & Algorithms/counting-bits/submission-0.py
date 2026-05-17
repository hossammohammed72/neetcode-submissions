class Solution:
    def countBits(self, n: int) -> List[int]:
        num1slist = []
        for i in range(n+1):
          num1slist.append( self.hammingWeight(i))
        return num1slist
    def hammingWeight(self, n: int) -> int:
        num1s=0
        while n > 0 :
            num1s +=n%2
            n = n//2
        return num1s
                
        