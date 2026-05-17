class Solution:
    def boom(self,nums,start,end,target)->int:
        print(start,end)
        if start>= end:
            if start == len(nums):
                return nums[0]
            return nums[end]
        mid = int((start+end)/2)
        if nums[mid] < target:
            target = nums[mid]
            end = mid
            return self.boom(nums,start,end,target)
        if nums[mid]>= target :
            start = mid+1
            return self.boom(nums,start,end,target)
    def findMin(self, nums: List[int]) -> int:
        return self.boom(nums,0,len(nums),nums[0])
    