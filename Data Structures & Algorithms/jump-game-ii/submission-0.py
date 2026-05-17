class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(currentIndex):
            if currentIndex >=(len(nums)-1):
                return 0
            if nums[currentIndex] ==0:
                return 1e6
            sol = 1e6
            for i in range(1,nums[currentIndex]+1):
                sol =  min(dfs(currentIndex+i)+1,sol)
            return sol
        return  dfs(0)
        