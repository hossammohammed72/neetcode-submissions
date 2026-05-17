class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combinationsMap = {}
        def dfs(i,currCombination,currSum):
            if currSum > target:
                return
            if currSum == target:
                if ','.join(str(v) for v in currCombination) in combinationsMap:
                    return
                combinationsMap[','.join(str(v) for v in currCombination)] = True

                combinations.append(currCombination)
                return 
            if i>=len(nums):
                return
            tempCombination = []
            tempCombination[:] = currCombination[:]
            currCombination = tempCombination 
            currCombination.append(nums[i])
            currSum+=nums[i]
            for j in range(i,len(nums)):
                dfs(j,currCombination,currSum)
        for i in range(len(nums)):
            dfs(i,[],0)
        return combinations
        