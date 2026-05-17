class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mem = {}
        for i in range(len(nums)):
            if nums[i] in mem:
                return nums[i]
            mem[nums[i]]= True

        