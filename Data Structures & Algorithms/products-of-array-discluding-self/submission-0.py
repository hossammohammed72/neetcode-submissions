from numpy import ones
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productRight = nums.copy()
        productLeft = nums.copy()
        productExcluded = nums.copy()
        for i in range(1,len(nums)):
            productRight[len(nums)-1-i] =  productRight[len(nums)-1-i]* productRight[len(nums)-i]
            productLeft[i]= productLeft[i]*productLeft[i-1] 
        productExcluded[0] = productRight[1]
        productExcluded[len(nums)-1] = productLeft[len(nums)-2]
        for i in range(1,len(nums)-1):
            productExcluded[i] = productRight[i+1]*productLeft[i-1]
        return productExcluded