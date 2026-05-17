from numpy import zeros
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i,len(temperatures)):
                if temperatures[j]-temperatures[i] > 0 and result[i]==0:
                    result[i] = int(j-i)

        return result
                    
        