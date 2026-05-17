class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_sorted = ''.join(sorted(s1))
        for r in range(len(s1),len(s2)+len(s1)):
            print(r,s2[l:r])
            s2_sorted = ''.join(sorted(s2[l:r]))
            if s1_sorted == s2_sorted:
                return True
            l+=1
        return False
        