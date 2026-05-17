class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookupList = {}
        indexList = {}
        for i,n in enumerate(nums):
            if n in lookupList and indexList[n] != i:
                return [indexList[n],i]
            lookupList[target-n] = n
            indexList[target-n] = i

        