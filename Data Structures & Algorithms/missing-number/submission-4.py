class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        mathSum = n*(n+1)//2
        actualSum = 0
        for i in range(len(nums)):
            actualSum+=nums[i]
        
        return mathSum-actualSum


        