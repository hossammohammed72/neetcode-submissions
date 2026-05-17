from numpy import zeros
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyArray = {}
        kMostFrequent = []
        for num in nums:
            if num in frequencyArray:
                frequencyArray[num]+=1
            else:
                frequencyArray[num]=1
        for i in range(k):
            biggestCurrentElementIndex =max(frequencyArray,key=frequencyArray.get) 
            kMostFrequent.append(biggestCurrentElementIndex)
            frequencyArray[biggestCurrentElementIndex] = 0
        return kMostFrequent
