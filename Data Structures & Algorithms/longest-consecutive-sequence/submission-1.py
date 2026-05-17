from numpy import zeros
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        biggestNumber = max(nums)
        smallestNumber = min(nums)
        includeOffset=False
        if smallestNumber < 0:
            biggestNumber = biggestNumber-smallestNumber
            includeOffset=True
        frequencyArray = zeros(biggestNumber+1)
        for num in nums:
            if includeOffset:
                num = num-smallestNumber
            frequencyArray[num] = 1
        consecutiveSequence=0
        maxConsecutiveSequence=0
        print(frequencyArray)
        for i in range(len(frequencyArray)):
            if frequencyArray[i] > 0:
                consecutiveSequence+=1
            else:
                if consecutiveSequence > maxConsecutiveSequence:
                    maxConsecutiveSequence=consecutiveSequence
                consecutiveSequence=0
        if consecutiveSequence > maxConsecutiveSequence:
                    maxConsecutiveSequence=consecutiveSequence
        return maxConsecutiveSequence
