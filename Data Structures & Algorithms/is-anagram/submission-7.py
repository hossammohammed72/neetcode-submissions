from numpy import zeros
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alpha = {}
        for ch in s:
            if ch in alpha: 
                alpha[ch] +=1
            else:
                alpha[ch] =1
        for ch in t:
            if ch in alpha and alpha[ch] >0:
                alpha[ch] -=1
            else:
                return False
        print(alpha)
        if sum(alpha.values()) == 0:
            return True
        else:
            return False


        