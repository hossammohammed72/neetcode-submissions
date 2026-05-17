class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def dfs(currentIndex):
            if currentIndex >= (len(nums)-1):
                return True
            if nums[currentIndex] == 0:
                return False
            result = False
            for i in range(1,nums[currentIndex]+1):
                result = result or dfs(currentIndex+i)
            return result
        return dfs(0)
        