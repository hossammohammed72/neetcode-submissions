class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        output = []
        chosenTriplets = {}
        print(nums)
        for i in range(len(nums)):
            j=i+1
            k=j+1
            while k > j and j> i and k<len(nums):
                print(i,j,k)
                if nums[i]+nums[j]+nums[k] == 0:
                    
                    validList = [nums[i],nums[j],nums[k]]
                    if  not ((str(nums[i])+'*'+str(nums[j])+'*'+str(nums[k])) in chosenTriplets):    
                        output.append(validList)
                        chosenTriplets[(str(nums[i])+'*'+str(nums[j])+'*'+str(nums[k]))]= 1
                    j = j+1
                    k = j+1
                elif nums[i]+nums[j]+nums[k] > 0:
                    j = j+1
                    k = j+1
                elif k == len(nums)-1 and j < len(nums)-2:
                    j = j+1
                    k = j+1
                else:
                    k+=1


        return output
                
        