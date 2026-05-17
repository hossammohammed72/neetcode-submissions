class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = []
        memo= {}
        def dfs(res,j):
            if j == len(nums):
                if res not in memo:
                    arr = res.split('*')
                    arr.pop()
                    subsets.append(arr)
                    memo[res] = True
                return 
            dfs(res+str(nums[j])+"*",j+1)            
            dfs(res,j+1)
            return
        dfs('',0)
        return subsets
        
        