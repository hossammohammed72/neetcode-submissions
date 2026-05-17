class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums,0,len(nums),target)
    def binarySearch(self,nums,start,end,target)-> int:
        print(start,end)
        if start >= end:
            if start == len(nums):
                return -1
            elif target == nums[start]:
                return start
            elif target == nums[end]:
                return end
            return -1
        mid = int((start+end)/2)
        if nums[mid] > target:
            if nums[start] > target:
                start = start+1
            else:
                end = mid-1
        elif nums[mid] < target:
            if (end == len(nums) and nums[end-1] < target) or \
                (end < len(nums) and nums[end] < target):
                end=end-1
            else:
                start = mid+1
        else:
            return mid
        return self.binarySearch(nums,start,end,target)
