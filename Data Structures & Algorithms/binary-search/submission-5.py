class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(start,end,target):
            if start >= end:
                if nums[end-1] == target:
                    return end
                else:
                    return -1
            mid = int((start+end)/2)
            print(mid,start,end)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(start,mid,target)
            else:
                return binarySearch(mid+1,end,target)
        return binarySearch(0,len(nums),target)
        
            