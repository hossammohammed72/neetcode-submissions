class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_sorted = self.stringHash(s1)
        for r in range(len(s1),len(s2)+len(s1)):
            s2_sorted = self.stringHash(s2[l:r])
            if s1_sorted == s2_sorted:
                return True
            l+=1
        return False
    def stringHash(self,s):
        stringSum = 0
        for i in range(len(s)):
            stringSum+= (ord(s[i])-ord("a")+2)**4
        print(stringSum,s)
        return stringSum
        